from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def batch_ingest():
    """Run batch ingestion process."""
    subprocess.call(["python", "data_ingestion/batch_data_ingestion.py"])

def stream_process():
    """Run stream processing."""
    subprocess.call(["python", "stream_processing/spark_stream_processing.py"])

def load_to_redshift():
    """Load data to Redshift."""
    subprocess.call(["python", "storage/redshift_connector.py"])

dag = DAG('data_lake_pipeline', start_date=datetime(2022, 1, 1), schedule_interval='@daily')

batch_task = PythonOperator(
    task_id='batch_ingestion_task',
    python_callable=batch_ingest,
    dag=dag,
)

stream_task = PythonOperator(
    task_id='stream_processing_task',
    python_callable=stream_process,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_to_redshift_task',
    python_callable=load_to_redshift,
    dag=dag,
)

batch_task >> stream_task >> load_task
