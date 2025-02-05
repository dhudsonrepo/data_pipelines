# End-to-End Real-Time Data Pipeline with PySpark, Snowflake, Airflow, and Databricks

This project demonstrates an end-to-end real-time data pipeline, where data is ingested, processed, and stored in a Snowflake data warehouse. The pipeline uses **Apache Airflow** for orchestration, **PySpark** for stream processing, and **Snowflake** for data storage and analytics. It is designed to handle real-time data with minimal latency, simulating data ingestion and processing, followed by automated orchestration of tasks.

## Project Overview

The pipeline consists of the following components:

1. **Data Ingestion**: Simulated sensor data is generated and written to a file to simulate real-time data streams.
2. **Stream Processing with PySpark**: The sensor data is processed using **Apache Spark** (via **PySpark**) to compute metrics like average temperature per sensor.
3. **Storage with Snowflake**: Processed data is then ingested into a **Snowflake** data warehouse for storage and future analysis.
4. **Orchestration with Apache Airflow**: **Apache Airflow** is used to orchestrate the entire process, managing task dependencies and scheduling.
5. **Data Transformation**: SQL queries are used within Snowflake to transform and analyze the processed data.

## Prerequisites

Ensure you have the following tools installed:
- **Python 3.x**
- **Apache Airflow**
- **PySpark**
- **Snowflake account** with credentials
- **Docker** (Optional, for containerizing components)
- **Databricks** account (Optional, for cloud-based Spark processing)

### Required Python Libraries
You can install the required dependencies using the `requirements.txt` file:

```bash
    pip install -r requirements.txt
```


### Running the Pipeline

1. Set up Snowflake


2. Configure the Pipeline
- Clone this repository to your local machine:
```bash
    git clone https://github.com/dhudsonrepo/real-time-data-pipeline.git
    cd real-time-data-pipeline
```
- Open storage/snowflake_connector.py and update it with your Snowflake connection details (e.g., user, password, account, etc.).

3. Running the Pipeline
- Step 1, Data Ingestion: Simulate real-time data ingestion by running the mock data generator script. This will generate JSON data and simulate a stream of sensor data.
```bash
  python data_ingestion/data_generator.py
```
- Step 2, Stream Processing (PySpark): Run the PySpark job to process the incoming data in real-time. This job will aggregate the sensor data and calculate the average temperature per sensor. If using Databricks, upload the spark_streaming_job.py to your cluster and run it there. Alternatively, you can run it locally if you have PySpark installed.
```bash
  python stream_processing/spark_streaming_job.py
```
- Step 3, Airflow Orchestration: **Apache Airflow** orchestrates the tasks in the pipeline, including data ingestion, processing, and loading into Snowflake. Install Airflow and set up the **DAG** (Directed Acyclic Graph) by configuring **airflow_dag.py**. Make sure the Airflow web server is running.

To start Airflow locally:
```bash
    export AIRFLOW_HOME=./airflow
    airflow db init
    airflow webserver --port 8080
    airflow scheduler
```
This will run the pipeline every minute, as defined in the DAG.

- Step 4, Data Loading to Snowflake: After processing, the data will be loaded into Snowflake via the snowflake_connector.py script.

- Step 5: (Optional) Data Transformation in Snowflake: Once data is in Snowflake, you can run SQL queries to perform data transformations and analytics.

Example SQL query in sql_queries/transformation.sql:
```
    -- Example transformation to calculate average temperature for each sensor over time
    SELECT
        sensor_id,
        AVG(temperature) AS avg_temperature
    FROM
        sensor_data
    WHERE
        timestamp >= '2023-01-01'
    GROUP BY
        sensor_id;
```
Run the above SQL query in your Snowflake environment to analyze the data.

## Docker (Optional)

You can use **Docker** to containerize the components of this pipeline, making it easier to deploy and run locally or in a cloud environment.

To run the pipeline in a containerized environment, use the following Docker setup:

1. Build the Docker images:
```bash
  docker build -t real-time-data-pipeline .
```

2. Run the Docker containers:
```bash
  docker-compose up
```
This should start all necessary services (Airflow, Kafka, Zookeeper, etc.) in Docker containers.

## How to Contribute
Feel free to fork this project and create pull requests with new features, improvements, or bug fixes. If you have suggestions or issues, please open an issue in the repository.
