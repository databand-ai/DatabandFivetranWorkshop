# Fivetran Astronomer Workshop


## Table of Contents
1. [Fivetran](#fivetran)
2. [Astronomer](#astronomer)
3. [Running you first DAG](#dag)

# Fivetran <a name="fivetran"></a>
This section guides the set up of a Fivetran trial this creates a BigQuery destionation to store data that is managed by Fivetran, Fivetran then automates the movement of data into this data warehouse.


| ![ft3.jpg](images/ft3.jpg) | 
|:--:| 
| To start a Fivetran trial, the **E-mail** and **Company** entered cannot have been used for a trial previously. To achieve this, I created an email for this workshop and used it as the Company as well. Select *Sign up* |

| ![ft4.jpg](images/ft4.jpg) | 
|:--:| 
| Select *Verify your Account* in an email from sales@fivetran.com |

| ![ft5.jpg](images/ft5.jpg) | 
|:--:| 
| Create a password and *Continue* |

| ![ft6.jpg](images/ft6.jpg) | 
|:--:| 
| A Fivetran trial account has been created! Just one connector will be used in this example, select *Set up a connector* |

| ![ft7.jpg](images/ft7.jpg) | 
|:--:| 
| Fivetran will move data from Google Sheets to a data destination, select *Google Sheets* and *CONTINUE SETUP*|

| ![ft8.jpg](images/ft8.jpg) | 
|:--:| 
| With the **Destination schema** as *google_sheets* and **Destination table** as *forestfires*, Fivetran knows where in BigQuery to store data, then select *Grant User Access* and *AUTHORIZE* to select a Google account the Fivetran can use to access the Google sheet. Any Google account will be able to. |

| ![ft9.jpg](images/ft9.jpg) | 
|:--:| 
| The **Sheet URL** is listed below, after copying it, select *alldata* for the **Named Range** and *SAVE & TEST*|

Google Sheet URL 
`https://docs.google.com/spreadsheets/d/1Xab8msuo00LKwAWzp1MoXjEgMuUxa4FVfyLipX0ocsA/edit?usp=sharing`

| ![ft10.jpg](images/ft10.jpg) | 
|:--:| 
| After all Connections tests have passed, select *CONTINUE* |

| ![ft11.jpg](images/ft11.jpg) | 
|:--:| 
| Now a new data warehouse will be created, managed and set up as a Fivetran Destination, select *I don't have one* and *CONTINUE SETUP* |



| ![ft11.jpg](images/ft14.jpg) | 
|:--:| 
| Copy the **Project ID** and send it to nick.acosta@fivetran.com, then select **CONTINUE** |

| ![ft15.jpg](images/ft15.jpg) | 
|:--:| 
| Finish Fivetran setup by selecting *Start Inital Sync* |
