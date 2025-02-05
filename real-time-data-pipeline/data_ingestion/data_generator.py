import random
import time
import json

# Simulate generating sensor data
def generate_sensor_data():
    return {
        "sensor_id": random.randint(1, 10),
        "temperature": round(random.uniform(15, 30), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "timestamp": int(time.time())
    }

# Save the generated data to a file (simulating real-time ingestion)
def save_data_to_file():
    while True:
        data = generate_sensor_data()
        with open("sensor_data.json", "a") as f:
            f.write(json.dumps(data) + "\n")
        time.sleep(1)

# Call the function to simulate real-time data generation
if __name__ == "__main__":
    save_data_to_file()
