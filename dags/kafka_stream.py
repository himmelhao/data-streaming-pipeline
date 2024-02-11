from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'hao',
    'start_date': datetime(2024, 2, 11),
} 

def stream_data():
    import json
    import requests

    res = requests.get("https://randomuser.me/api/")
    print(res.json())

with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='streaming_task',
        python_callable=stream_data
    )

stream_data()

