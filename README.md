# Fivetran Astronomer Workshop


## Table of Contents
1. [Fivetran](#fivetran)
2. [Astronomer](#astronomer)
3. [Running you first DAG](#dag)

# Fivetran <a name="fivetran"></a>
This section guides the set up of a Fivetran trial this creates a BigQuery destionation to store data that is managed by Fivetran, Fivetran then automates the movement of data into this data warehouse.


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
