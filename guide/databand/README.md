# Databand <a name="integrate-databand-with-apache-airflow"></a> 

###Overview

By the end of this guide, we will have accomplished:
* Accessing your Databand environment
* Creating an Airflow Syncer in the Databand UI
* Create and configure the `dbnd_config` connection in Airflow UI
* Deploy `databand_monitor_dag` to GCS
* Enable Databand monitoring in Apache Airflow

###Prerequisites
1. Completed the preceding modules:
   * [Fivetran](https://github.com/databand-ai/DatabandFivetranWorkshop/tree/master/guide/fivetran#fivetran)
   * [Apache Airflow](https://github.com/databand-ai/DatabandFivetranWorkshop/tree/master/guide/apache-airflow#apache-airflow)
   * [Running your first DAG](https://github.com/databand-ai/DatabandFivetranWorkshop/tree/master/guide/dag#running-your-first-dag)
2. Received an email containing your Databand URL and credentials.
   * If you are unable to locate this email, please contact the workshop host(s) for assistance.

### Tips for Success
* For best results, complete the following steps in the order they are presented.
* All instructions reference the screenshot immediately preceding the instruction text.
* Reach out to your host(s) with any questions regarding the instructions presented in this guide.

### Instructions

| ![databand1.png](../../images/databand1.png) |
|:--:|
| Copy/paste your Databand URL from your email into your favorite web browser |
| **PRO-TIP** - Google Chrome or Mozilla Firefox are recommended for the best user experience |
| Enter your Databand credentials provided in the email |
| Click **LOGIN** |

| ![databand2.png](../../images/databand2.png) |
|:--:|
| Next, let's add an Airflow Syncer to receive metadata from Composer |
| In the bottom left of the Databand Dashboard, click the circular avatar icon (1) |
| Click **Settings** (2) to open your environment settings |

| ![databand3.png](../../images/databand3.png) |
|:--:|
| Click **Airflow Syncer** (1) in the Settings menu |
| Click the purple **+ Add** button (2) to begin configuring an Airflow Syncer |

| ![databand4.png](../../images/databand4.png) |
|:--:|
| For **Airflow mode**, select **Google Composer (Airflow 1.x)**  |
| In **Airflow URL**, enter the **URL** for **your Cloud Composer UI** |
| URL Format Example: `https:///xxxxx-tp.appspot.com/` |
| In **Syncer Name**, input `observability_workshop` |
| Click **Save** and **Do Not Close The Following Information Screen** |

| ![databand5.png](../../images/databand5.png) ![databand6.png](../../images/databand6.png) |
|:--:|
| In the Airflow UI, navigate to **Admin >> Connections** and add a new `HTTP` connection |
| From the **Databand Information Screen**, copy the **Conn Id** and **Extra** information to the Airflow UI |
| Click **Save** in Airflow and **OK** in Databand |

| ![databand7.png](../../images/databand7.png) |
|:--:|
| Navigate to the **GCS Bucket details** page and click **UPLOAD FILES** |
| Select the [`databand_airflow_monitor.py`](https://github.com/databand-ai/DatabandFivetranWorkshop/tree/master/dags/databand_airflow_monitor.py) file located in the `/DatabandFivetranWorkshop/dags/` directory |
| Click **Create** |

| ![databand8.png](../../images/databand8.png) |
|:--:|
| In the **Airflow UI**, click the radio button next to `databand_airflow_monitor` to enable the DAG (1) |
| Once enabled, `databand_airflow_monitor` will begin running automatically. Depending on Composer available resources, this may take a few minutes |

### Next Steps
[Observability: Creating Action from Error](https://github.com/databand-ai/DatabandFivetranWorkshop/tree/master/guide/observability#observability-)

