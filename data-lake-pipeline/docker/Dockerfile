# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8080 available to the world outside the container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run pipeline when the container launches
CMD ["python", "data_ingestion/real_time_data_ingestion.py"]
