from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.etl_pipeline import run_etl

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 1),
    'retries': 1,
}

dag = DAG(
    'ecommerce_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag
)

etl_task
