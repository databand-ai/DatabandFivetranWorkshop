# Running your first DAG 

Start Astronomer with the following command as use this part of the command to finish setting it up to run your first DAG

`astro dev start`

Note: are you seeing `buildkit not supported by deamon Error`? See [this guide](https://forum.astronomer.io/t/buildkit-not-supported-by-daemon-error-command-docker-build-t-airflow-astro-bcb837-airflow-latest-failed-failed-to-execute-cmd-exit-status-1/857).

| ![astro1.png](../../images/astro1.png) |
|:--:|
| Find Astronomer at [localhost:8080](localhost:8080), then enter the **Username** *admin* and **Password** *admin*, then select **Sign In**|

| ![astro2.png](../../images/astro2.png) |
|:--:|
| Find the **Admin** section, then select **Connections** |

| ![astro3.png](../../images/astro3.png) |
|:--:|
| The following information should be filled out to connect Fivetran and Astronomer, Fivetran's API Key and API Secret can be found in the next slide  |

| ![astro3.1.png](../../images/astro3.1.png) |
|:--:|
| At [fivetran.com/account/settings](fivetran.com/account/settings), copy the **API key** and **API secret** and paste into Astronomer |

| ![astro4.png](../../images/astro4.png) |
|:--:|
| For the Google Cloud connection, you will receive an email with your keyfile json and instructions on how to use it |

| ![astro5.png](../../images/astro5.png) |
|:--:|
| In **Admin**, find **Variables** section and edit the 2 that are created for you |

https://fivetran.com/dashboard/connectors/google_sheets/google_sheets.forestfires/setup

| ![astro5.1.png](../../images/astro5.1.png) |
|:--:|
| At *https://fivetran.com/dashboard/connectors/google_sheets/google_sheets.forestfires/setup*, the **Fivetran Connector ID** should be copy and pasted in Astronomer as **connector_id** |

| ![astro6.png](../../images/astro6.png) |
|:--:|
| Back in Astronomer, everything is ready, select the example DAG, Unpause with the button on the left, then trigger it with the button on the right |
