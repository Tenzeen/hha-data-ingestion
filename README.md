Code Explanation
Section 1: Importing xls file
Found datasets from Kaggle and combined them on Excel.
Used pandas to import data from tab1 and tab2 into a dataframe.

python
Copy code
# Reading and importing tab1 using pandas
tab1 = pd.read_excel('/Users/tenzi/Documents/Github/hha-data-ingestion/data/data.xlsx', sheet_name='tab1')

# Reading and importing tab2 using pandas
tab2 = pd.read_excel('/Users/tenzi/Documents/Github/hha-data-ingestion/data/data.xlsx', sheet_name='tab2')
Section 2: Requests package to bring in CMS dataset
Found API dataset on CMS website.
Used requests to bring in CMS JSON API.

python
Copy code
# Bringing in CMS JSON API using requests
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/8d900ef4-0571-42d0-bc8f-82dcf1b5f4c7/data')

# Converting JSON data to Python object
apiDataset = apiDataset.json()
Section 3: BigQuery
BigQuery 1
Used JSON authentication key to create a client that connects to Google BigQuery. Query/access the first 100 rows of the selected public dataset on Google BigQuery. Retrieve results from the query and put them into a dataframe.

python
Copy code
# Creating a client that connects to Google BigQuery using a JSON authentication key
client = bigquery.Client.from_service_account_json('/Users/tenzi/Documents/GitHub/hha-data-ingestion/bigquery/tenzin-507-a1863ba676b3.json')

# Querying a public dataset on Google BigQuery and retrieving the first 100 rows
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips` LIMIT 100")

# Storing the results in a pandas dataframe
results = query_job.result()
bigquery1 = pd.DataFrame(results.to_dataframe())
BigQuery 2
Querying a public dataset on Google BigQuery and retrieving the first 100 rows. Storing the results in a pandas dataframe.

python
Copy code
# Querying a public dataset on Google BigQuery and retrieving the first 100 rows
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100")

# Storing the results in a pandas dataframe
results = query_job.result()
bigquery2 = pd.DataFrame(results.to_dataframe())
