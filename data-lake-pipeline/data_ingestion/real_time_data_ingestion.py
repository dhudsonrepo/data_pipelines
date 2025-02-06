from kafka import KafkaProducer
import json
import time

def get_data():
    """Simulate reading data from an IoT device."""
    return {"device_id": "1234", "temperature": 22.5, "humidity": 60}

def produce_data():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    while True:
        data = get_data()
        producer.send('iot_data_topic', value=data)
        print(f"Sent: {data}")
        time.sleep(5)

if __name__ == "__main__":
    produce_data()

