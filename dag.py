from airflow import DAG, AirflowException
from airflow.decorators import task
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import datetime
from airflow.models import Variable
from airflow.sensors.sql import SqlSensor
from airflow.operators.sql import SQLCheckOperator
from airflow.utils.task_group import TaskGroup
from fivetran_provider.operators.fivetran import FivetranOperator
from fivetran_provider.sensors.fivetran import FivetranSensor

import hashlib
import json
import logging


# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    "owner": "astronomer",
    "depends_on_past": False,
    "start_date": datetime(2021, 7, 7),
    "email": ["noreply@astronomer.io"],
    "email_on_failure": False
}

with DAG("lab_dag",
         default_args=default_args,
         description="",
         schedule_interval=None,
         catchup=False) as dag:
    """
    ### Simple EL Pipeline with Data Integrity and Quality Checks 3
    This is the third in a series of DAGs showing an EL pipeline with data integrity
    and data quality checking. A single file is uploaded to S3, then its ETag is
    verified against the MD5 hash of the local file. The two should match, which
    will allow the DAG to continue to the next task. A second data load from S3
    to Redshift is triggered, which is followed by another data integrity check.
    If the check fails, an Airflow Exception is raised. Otherwise, a final data
    quality check is performed on the Redshift table per row for a subset of rows,
    immitating a row-based data quality spot check where the specific ground truth
    is known.
    Before running the DAG, set the following in an Airflow or Environment Variable:
    - key: aws_configs
    - value: { "s3_bucket": [bucket_name], "s3_key_prefix": [key_prefix], "redshift_table": [table_name]}
    Fully replacing [bucket_name], [key_prefix], and [table_name].
    What makes this a simple data quality case is:
    1. Absolute ground truth: the local CSV file is considered perfect and immutable.
    2. No transformations or business logic.
    3. Exact values of data to quality check are known.
    This demo solves the issue simple_el_2 left open: quality checking the data
    in the uploaded file. This DAG is a good starting point for a data integrity
    and data quality check.
    """



    """
    #### FivetranOperator & FivetranSensor
    Calling Fivetran to begin data movement from Google Sheets to BigQuery
    The FivetranSensor monitors the status of the Fivetran data sync
    """
    fivetran_sync_start = FivetranOperator(
    task_id='fivetran-task',
    fivetran_conn_id='fivetran_default',
    connector_id="{{ var.value.get('connector_id') }}",
    dag=dag
)

fivetran_sync_wait = FivetranSensor(
    task_id='fivetran-sensor',
    fivetran_conn_id='fivetran_default',
    connector_id="{{ var.value.get('connector_id') }}",
    poke_interval=5,
    dag=dag
)


    """
    #### BigQuery row validation task
    Ensure that data was copied to BigQuery correctly. A SQL Sensor is
    used here to check for any files in the stl_load_errors table. If the failure
    callback (above) is triggered, the query number is printed to the task log.
    """
    validate_bigquery = SqlSensor(
        task_id="validate_bigquery",
        conn_id="redshift_default",
        sql="sql/validate_forestfire_redshift_load.sql",
        params={"filename": CSV_FILE_NAME},
        failure=redshift_load_error
    )

    """
    #### Row-level data quality check
    Run a data quality check on a few rows, ensuring that the data in BigQuery
    matches the ground truth in the correspoding JSON file.
    """
    with open("include/validation/forestfire_validation.json") as ffv:
        with TaskGroup(group_id="row_quality_checks") as quality_check_group:
            ffv_json = json.load(ffv)
            for id, values in ffv_json.items():
                values["id"] = id
                values["redshift_table"] = Variable.get("aws_configs", deserialize_json=True).get("redshift_table")
                SQLCheckOperator(
                    task_id=f"forestfire_row_quality_check_{id}",
                    conn_id="redshift_default",
                    sql="sql/forestfire_row_quality_check.sql",
                    params=values,
                )

    done = DummyOperator(task_id="done")

    fivetran_operator >> fivetran_sensor >> validate_bigquery
    validate_bigquery >> quality_check_group
    quality_check_group >> done
