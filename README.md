# Fivetran Astronomer Workshop


## Table of Contents
1. [Fivetran](#fivetran)
2. [Astronomer](#astronomer)
3. [Running your first DAG](#dag)

# Fivetran <a name="fivetran"></a>
This section guides the set up of a Fivetran trial this creates a BigQuery destination to store data that is managed by Fivetran, Fivetran then automates the movement of data into this data warehouse.


| ![ft1.png](images/ft1.png) |
|:--:|
| To start a Fivetran trial, the **E-mail** and **Company** entered cannot have been used for a trial previously. To achieve this, I created an email for this workshop and used it as the Company as well. Select *Sign up* |

| ![ft2.png](images/ft2.png) |
|:--:|
| Select *Verify your Account* in an email from sales@fivetran.com |

| ![ft3.png](images/ft3.png) |
|:--:|
| After creating a password, a Fivetran trial account has been created! Just one connector will be used in this example, select *Set up a connector* |

| ![ft4.png](images/ft4.png) |
|:--:|
| Fivetran will move data from Google Sheets to a data destination, select *Google Sheets* and *CONTINUE SETUP*|

| ![ft5.png](images/ft5.png) |
|:--:|
| With the **Destination schema** as *google_sheets* and **Destination table** as *forestfires*, Fivetran knows where in BigQuery to store data, then select *Grant User Access* and *AUTHORIZE* to select a Google account the Fivetran can use to access the Google sheet. Any Google account will be able to. |

| ![ft6.png](images/ft6.png) |
|:--:|
| The **Sheet URL** is listed below, after copying it, select *alldata* for the **Named Range** and *SAVE & TEST*|

Google Sheet URL
`https://docs.google.com/spreadsheets/d/1Xab8msuo00LKwAWzp1MoXjEgMuUxa4FVfyLipX0ocsA/edit?usp=sharing`

| ![ft7.png](images/ft7.png) |
|:--:|
| After all Connections tests have passed, select *CONTINUE* |

| ![ft8.png](images/ft8.png) |
|:--:|
| Now a new data warehouse will be created, managed and set up as a Fivetran Destination, select *I don't have one* and *CONTINUE SETUP* |

| ![ft9.png](images/ft9.png) |
|:--:|
| These can be left unedited, select **CONTINUE** |

| ![ft10.png](images/ft10.png) |
|:--:|
| Copy the **Project ID** and send it to nick.acosta@fivetran.com, then select **CONTINUE** |

| ![ft10.png](images/ft11.png) |
|:--:|
| Finish Fivetran setup by selecting *Start Inital Sync* |

# Astronomer <a name="astronomer"></a>

Follow the guide in the link below to get started with Astronomer.
https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart

Stop before reaching **Step 3: Initialize an Airflow Project**, a project was been initalized for you

Clone and cd into it with the following commands

`git clone https://github.com/fivetran/FivetranAstronomerWorkshop`
`cd FivetranAstronomerWorkshop`

# Running your first DAG <a name="dag"></a>

Start Astronomer with the following command as use this part of the command to finish setting it up to run your first DAG

`astro dev start`

| ![astro1.png](images/astro1.png) |
|:--:|
| Find Astronomer at *localhost:8080*, then enter the **Username** *admin* and **Password** *admin*, then select **Sign In**|

| ![astro2.png](images/astro2.png) |
|:--:|
| Find the **Admin** section, then select **Connections** |

| ![astro3.png](images/astro3.png) |
|:--:|
| The following information should be filled out to connect Fivetran and Astronomer, Fivetran's API Key and API Secret can be found in the next slide  |

| ![astro3.1.png](images/astro3.1.png) |
|:--:|
| At *fivetran.com/account/settings*, copy the **API key** and **API secret** and paste into Astronomer |

| ![astro4.png](images/astro4.png) |
|:--:|
| For the Google Cloud connection, you will receive an email with your keyfile json and instructions on how to use it |

| ![astro5.png](images/astro5.png) |
|:--:|
| In **Admin**, find **Variables** section and edit the 2 that are created for you |

https://fivetran.com/dashboard/connectors/google_sheets/google_sheets.forestfires/setup

| ![astro5.1.png](images/astro5.1.png) |
|:--:|
| At *https://fivetran.com/dashboard/connectors/google_sheets/google_sheets.forestfires/setup*, the **Fivetran Connector ID** should be copy and pasted in Astronomer as **connector_id** |

| ![astro6.png](images/astro6.png) |
|:--:|
| Back in Astronomer, everything is ready, select the example DAG, Unpause with the button on the left, then trigger it with the button on the right |
