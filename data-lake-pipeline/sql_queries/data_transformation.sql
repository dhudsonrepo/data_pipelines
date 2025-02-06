-- Example transformation: Aggregating the temperature data per device
CREATE TABLE transformed_data AS
SELECT device_id, AVG(temperature) AS avg_temperature
FROM my_table
GROUP BY device_id;
