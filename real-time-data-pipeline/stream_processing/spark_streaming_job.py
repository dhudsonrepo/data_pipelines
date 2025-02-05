from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("SensorDataStream") \
    .getOrCreate()

# Read the data stream from a JSON file (simulating real-time data ingestion)
sensor_data_stream = spark \
    .readStream \
    .json("path/to/sensor_data.json")  # Replace with actual path to the data stream

# Process the data: Calculate average temperature per sensor
processed_stream = sensor_data_stream \
    .groupBy("sensor_id") \
    .agg({"temperature": "avg"}) \
    .withColumnRenamed("avg(temperature)", "avg_temperature")

# Write processed data to Snowflake (or any other destination)
processed_stream.writeStream \
    .outputMode("complete") \
    .format("snowflake") \
    .option("sfURL", "snowflake_account_url") \
    .option("sfDatabase", "your_database") \
    .option("sfSchema", "your_schema") \
    .option("sfWarehouse", "your_warehouse") \
    .option("sfRole", "your_role") \
    .option("dbtable", "sensor_data_avg") \
    .start()

spark.streams.awaitAnyTermination()
