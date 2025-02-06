import boto3
import os

def upload_to_s3(bucket_name, file_name, s3_path):
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, s3_path)
    print(f"File {file_name} uploaded to {s3_path}")

def main():
    file_name = 'batch_data.csv'  # Example batch file
    bucket_name = 'my-bucket'
    s3_path = 'batch_data/2022-01-01.csv'
    upload_to_s3(bucket_name, file_name, s3_path)

if __name__ == "__main__":
    main()

