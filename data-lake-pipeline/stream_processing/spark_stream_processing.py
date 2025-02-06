from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def process_stream():
    spark = SparkSession.builder \
        .appName("Real-Time Stream Processing") \
        .getOrCreate()

    # Define Kafka stream source
    kafka_stream = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "iot_data_topic") \
        .load()

    # Deserialize JSON message
    df = kafka_stream.selectExpr("CAST(value AS STRING)") \
        .select(from_json("value", "struct<device_id:string, temperature:float, humidity:int>").alias("data")) \
        .select("data.*")

    # Process data (e.g., filtering, transformations)
    df_filtered = df.filter(col("temperature") > 20)

    # Write to S3
    query = df_filtered \
        .writeStream \
        .outputMode("append") \
        .format("json") \
        .option("checkpointLocation", "/tmp/checkpoint") \
        .option("path", "s3a://my-bucket/processed_data/") \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    process_stream()
