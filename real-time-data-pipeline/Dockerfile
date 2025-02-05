# Base image for PySpark environment
FROM openjdk:8-jdk-alpine

# Install dependencies
RUN apk add --no-cache python3 py3-pip bash

# Install required Python packages
RUN pip3 install pyspark snowflake-connector-python

# Copy the project files into the container
COPY . /app
WORKDIR /app

# Command to run the ingestion script
CMD ["python3", "data_ingestion/data_generator.py"]
