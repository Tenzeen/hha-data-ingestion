The purpose of this assignment was to practice ingesting data using Python.

The python script reads data from different sources and stores it in pandas dataframes. The script has three main sections, each of which serves a different purpose.

In Section 1, the script imports data from two sheets named "tab1" and "tab2" of an Excel file using the pandas library. The two sheets are located in the same file called "data.xlsx". The imported data is stored in two pandas dataframes called "tab1" and "tab2".

In Section 2, the script uses the requests library to bring in a JSON API dataset from the CMS website. The data is requested from the URL "https://data.cms.gov/data-api/v1/dataset/8d900ef4-0571-42d0-bc8f-82dcf1b5f4c7/data" and stored in a variable called "apiDataset". The JSON data is then converted to a Python object using the json library.

In Section 3, the script connects to Google BigQuery using the google-cloud-bigquery library. In BigQuery 1, the script queries a public dataset named "bigquery-public-data.chicago_taxi_trips.taxi_trips" and retrieves the first 100 rows. The results are stored in a pandas dataframe called "bigquery1". In BigQuery 2, the script queries a public dataset named "bigquery-public-data.chicago_crime.crime" and retrieves the first 100 rows. The results are stored in a pandas dataframe called "bigquery2".
