from pyspark.sql import SparkSession

def batch_process_data():
    spark = SparkSession.builder \
        .appName("Batch Data Processing") \
        .getOrCreate()

    # Read batch data from S3
    df = spark.read.option("header", "true").csv("s3a://my-bucket/batch_data/*.csv")

    # Example transformation: Filtering and Aggregating
    df_filtered = df.filter(df['temperature'] > 20)
    df_aggregated = df_filtered.groupBy("device_id").agg({"temperature": "avg"})

    # Write the processed data back to S3
    df_aggregated.write.format("csv").save("s3a://my-bucket/processed_batch_data/")

if __name__ == "__main__":
    batch_process_data()
