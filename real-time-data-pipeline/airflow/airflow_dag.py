from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

from data_ingestion.data_generator import save_data_to_file
from stream_processing.spark_streaming_job import process_sensor_data
from storage.snowflake_connector import load_data_to_snowflake

# Define the Airflow DAG
dag = DAG(
    'real_time_data_pipeline',
    description='A real-time data pipeline with PySpark, Airflow, Snowflake',
    schedule_interval='* * * * *',  # Runs every minute
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

# Define the tasks
data_ingestion_task = PythonOperator(
    task_id='ingest_data',
    python_callable=save_data_to_file,
    dag=dag,
)

spark_processing_task = PythonOperator(
    task_id='process_spark_stream',
    python_callable=process_sensor_data,
    dag=dag,
)

snowflake_load_task = PythonOperator(
    task_id='load_data_to_snowflake',
    python_callable=load_data_to_snowflake,
    op_args=['processed_data_df', 'sensor_data_avg'],
    dag=dag,
)

# Set task dependencies
data_ingestion_task >> spark_processing_task >> snowflake_load_task
