from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from datetime import datetime
from reddit_etl import reddit_extract

args = {
	'owner' : 'airflow', 
	'start_date' : datetime(2020, 11, 8), 
	'email' : ['vinamrgrover@gmail.com'], 	
	'email_on_failure' : False, 
	'email_on_retry' : False,  
	'retries' : 1,  
	'retry_delay' : timedelta(minutes = 1)
}									

dag = DAG(
	'ETL_DAG',  
	default_args = args,  
	description = 'Reddit extraction'
	)
																
task_1 = PythonOperator(	
	task_id = 'ETLreddit', 
	dag = dag, 
	python_callable = reddit_extract
	)
						
task_1
