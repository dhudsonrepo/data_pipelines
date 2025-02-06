import boto3

def upload_file_to_s3(local_file, bucket_name, s3_path):
    s3 = boto3.client('s3')
    s3.upload_file(local_file, bucket_name, s3_path)
    print(f"File {local_file} uploaded to S3://{bucket_name}/{s3_path}")

def download_file_from_s3(bucket_name, s3_path, local_file):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, s3_path, local_file)
    print(f"File {s3_path} downloaded to {local_file}")

if __name__ == "__main__":
    upload_file_to_s3('local_file.csv', 'my-bucket', 'batch_data/2022-01-01.csv')
