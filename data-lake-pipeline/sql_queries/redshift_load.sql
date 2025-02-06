-- Load data from S3 into a Redshift table
COPY my_table
    FROM 's3://my-bucket/processed_data/'
    IAM_ROLE 'arn:aws:iam::your-account-id:role/RedshiftRole'
    FORMAT AS CSV
    IGNOREHEADER 1;
