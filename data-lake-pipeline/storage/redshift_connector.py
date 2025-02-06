import boto3
import psycopg2

def load_data_to_redshift():
    # Redshift connection
    conn = psycopg2.connect(
        host="redshift-cluster-1.xxxxxxx.us-west-2.redshift.amazonaws.com",
        database="dev",
        user="awsuser",
        password="password"
    )
    cursor = conn.cursor()

    # Copy data from S3 to Redshift
    copy_query = """
    COPY my_table
    FROM 's3://my-bucket/processed_batch_data/'
    IAM_ROLE 'arn:aws:iam::your-account-id:role/RedshiftRole'
    FORMAT AS CSV;
    """

    cursor.execute(copy_query)
    conn.commit()
    print("Data loaded into Redshift.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    load_data_to_redshift()
