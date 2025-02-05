import snowflake.connector

def connect_to_snowflake():
    conn = snowflake.connector.connect(
        user='your_user',
        password='your_password',
        account='your_account',
        warehouse='your_warehouse',
        database='your_database',
        schema='your_schema'
    )
    return conn

def load_data_to_snowflake(df, table_name):
    conn = connect_to_snowflake()
    cursor = conn.cursor()

    # Example: Loading processed data to Snowflake
    for index, row in df.iterrows():
        cursor.execute(f"INSERT INTO {table_name} (sensor_id, avg_temperature) VALUES ({row['sensor_id']}, {row['avg_temperature']})")

    cursor.close()
    conn.close()

# Example: Using this function to load processed data
# load_data_to_snowflake(processed_data_df, 'sensor_data_avg')
