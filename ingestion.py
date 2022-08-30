#import packages
import pandas as pd #for general file types
import json #for json files
import requests #for web requests
import xlrd #for excel files
from google.cloud import bigquery #for bigquery




#***Section 1: Importing xls file****
#Found datasets from Kaggle and combined them on Excel.
#Used pandas to import data from tab1 and tab2 into a dataframe.

#Reading and importing tab1 using pandas
tab1 = pd.read_excel('/Users/tenzi/Documents/Github/hha-data-ingestion/data/data.xlsx', sheet_name='tab1')

#Reading and importing tab2 using pandas
tab2 = pd.read_excel('/Users/tenzi/Documents/Github/hha-data-ingestion/data/data.xlsx', sheet_name='tab2')




#***Section 2: Requests package to bring in CMS dataset***
#Found api dataset on CMS website.
#Used requests to bring in cms json API.
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/8d900ef4-0571-42d0-bc8f-82dcf1b5f4c7/data')

apiDataset = apiDataset.json()





#***Section 3: BigQuery***

#Bigquery 1
#Used json authentication key to create a client that connects to Google BigQuery
client = bigquery.Client.from_service_account_json('/Users/tenzi/Documents/GitHub/hha-data-ingestion/bigquery/tenzin-507-a1863ba676b3.json')

#Query/access the first 100 rows of the selected public dataset on Google BigQuery. 
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips` LIMIT 100") 

#Retrieve results from the query
results = query_job.result()

#Put results into dataframe
bigquery1 = pd.DataFrame(results.to_dataframe())


#Bigquery 2
#Query/access the first 100 rows of the selected public dataset on Google BigQuery. 
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100")

#Retrieve results from the query
results = query_job.result()

#Put results into dataframe
bigquery2 = pd.DataFrame(results.to_dataframe())