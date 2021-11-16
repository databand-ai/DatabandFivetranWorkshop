# Apache Airflow

###Overview
By the end of this guide, we will have accomplished:
* Confirm receipt of the following Airflow environment details
  * Apache Airflow URL
  * Apache Airflow Credentials
* Access Apache Airflow Airflow UI
* Access Apache Airflow `dags/` directory
* Create `credentials` directory within `dags/` directory

###Prerequisites
1. Upon your enrollment in this workshop, an Apache Airflow environment was created for you 
   * For this workshop, we will be using GCP's managed Apache Airflow Service: Cloud Composer
2. Please check your registration email for an email containing the following information:
    * Apache Airflow Credentials (**Google Account**)
    * Apache Airflow URL (**Cloud Composer**)
    * Apache Airflow `dags/` directory location (**Google Cloud Storage**)
    * If you are unable to locate this email, please contact the workshop host(s) for assistance.

### Tips for Success
* For best results, complete the following steps in the order they are presented.
* All instructions reference the screenshot immediately preceding the instruction text.
* Reach out to your host(s) with any questions regarding the instructions presented in this guide.

###Instructions
  
| ![composer1.png](../../images/composer1.png) ![composer2.png](../../images/composer2.png) |
|:--:|
| Copy/paste your Apache Airflow URL into your preferred browser and press 'Enter' |
| Follow the on screen Sign In instructions by entering your Apache Airflow Credentials |


| ![airflow1.png](../../images/airflow1.png) |
|:--:|
| Upon logging into Apache Airflow, you should see the Apache Airflow Webserver home page |
| **PROTIP** - You can always return this page by clicking the **Apache Airflow logo** (upper left) or the **DAGs** option in the navigation menu |


| ![composer3.png](../../images/composer3.png) |
|:--:|
| After confirming access to Apache Airflow, enter the provided GCS URL for your Apache Airflow `dags/` directory |
| With proper access, you should see a GCS bucket with a single object - Cloud Composer's airflow_monitoring.py file |


| ![composer4.png](../../images/composer4.png) ![composer5.png](../../images/composer5.png) |
|:--:|
| To confirm edit rights, click **Create Folder** |
| Name the new folder `credentials` |
| Click **Create** |


| ![composer6.png](../../images/composer6.png) |
| Before continuing, confirm you see both objects in your bucket: |
| 1. `airflow_monitoring.py` file |
| 2. `credentials` folder |


### Next Step
[Running your first DAG](https://github.com/databand-ai/DatabandFivetranWorkshop/tree/master/guide/dag#running-your-first-dag)

