# Data Lake Pipeline

This project is a complete data pipeline for ingesting, processing, and storing data. It utilizes various technologies including Apache Kafka, Spark, AWS S3, Redshift, and Airflow to automate data ingestion, processing, and loading into a data lake for further analysis.

The pipeline is designed to handle both **batch and real-time data** and supports orchestrating tasks using **Apache Airflow**. In this guide, we'll go through the steps required to set up and run the pipeline.

## Technologies Used
- **Apache Kafka**: For real-time data streaming.
- **Apache Spark**: For batch and stream data processing.
- **AWS S3**: For data storage.
- **Redshift**: For data warehouse storage.
- **Airflow**: For orchestrating and scheduling the pipeline.
- **Docker Compose**: For managing all services locally.

## Prerequisites

Before you begin, ensure that you have the following installed:
- **Docker** (with Docker Compose)
- **Python 3.8+**
- **AWS CLI** (if you're using AWS services)

Additionally, you’ll need Docker for local setup and orchestration.

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
    git clone https://github.com/dhudsonrepo/data-lake-pipeline.git
    cd data-lake-pipeline
```

### 2. Install Python Dependencies
Create a virtual environment (recommended but optional) and install the necessary dependencies:
```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  pip install -r requirements.txt
```

### 3. Run Docker Compose
The project uses Docker Compose to orchestrate various services like Kafka, Airflow, and MinIO (local S3).
```bash
  docker-compose up
```
This should:

- Start Zookeeper and Kafka for streaming data ingestion.
- Start Spark for processing the data.
- Start Airflow to schedule and manage tasks.
- Start MinIO to emulate AWS S3 for testing (replace with actual S3 when ready).

Once all services are up, the following ports will be exposed:

- Kafka: 9093
- Airflow: 8081 (Web UI)
- MinIO: 9000 (Local S3 UI)

### 4. Running the Data Pipeline
**Real-Time Data Ingestion**

The real-time data ingestion is handled by the Kafka service. To send data, run the real_time_data_ingestion.py script:
```bash
  python data_ingestion/real_time_data_ingestion.py
```
This will ingest real-time data into the pipeline via Kafka.

**Batch Data Ingestion**

For batch data ingestion, run the **batch_data_ingestion.py** script:
```bash
  python data_ingestion/batch_data_ingestion.py
```
This will ingest batch data into the pipeline.

**Stream Processing**

To process the ingested real-time data, run the **spark_stream_processing.py** script:
```bash
  python stream_processing/spark_stream_processing.py
```
This will process the data streams in Spark.

**Batch Processing**

For processing batch data, you can use:
```bash
  python stream_processing/batch_processing.py
```
This will process batch data from the S3 bucket and perform any required transformations.

**Load Data into Redshift**

Once data is processed, it needs to be loaded into Redshift for analysis. Run the redshift_connector.py script to load the processed data from S3 into Redshift:
```bash
  python storage/redshift_connector.py
```

### 5. Orchestrating with Apache Airflow
To manage and automate the entire pipeline, Airflow is used for task orchestration. Airflow will schedule and run tasks like batch ingestion, stream processing, and loading data into Redshift.

1. Start Airflow Web UI by visiting http://localhost:8081 in your browser.
2. Login to Airflow using the default credentials (airflow/airflow).
3. The pipeline will run according to the DAG defined in pipeline_dag.py.

Airflow will manage tasks in the following order:

- Batch Data Ingestion
- Stream Data Processing
- Loading Data to Redshift

You can trigger, pause, or monitor the progress of tasks through the Airflow UI.

### 6. Using MinIO (Optional Local S3)
   MinIO is a local emulation of AWS S3, which is used for storing data during development.

### 7. Docker Compose Commands
   To bring up the services:
```bash
  docker-compose up
```
To stop the services:

```bash
  docker-compose down
```

To rebuild and restart the services:

```bash
  docker-compose up --build
```

## Notes
- AWS Services: For production, replace the local MinIO service with AWS S3 and AWS Redshift.
- Data Formats: The pipeline currently assumes data is in CSV format. Ensure the incoming data matches the expected format or adjust the code to handle other formats (like Parquet or JSON).
- Airflow Setup: If you're running this pipeline on a cloud-based machine, ensure that you properly set up Airflow to use a cloud-based database for metadata storage (e.g., PostgreSQL or MySQL).
## Troubleshooting
- Kafka Issues: Ensure Kafka and Zookeeper are up and running. Check logs for any errors.
- Spark Issues: Ensure that the Spark cluster is properly set up and can connect to Kafka.
- Redshift Loading Issues: Ensure the Redshift credentials and IAM role are correctly configured for S3 access.