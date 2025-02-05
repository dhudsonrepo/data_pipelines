-- Example transformation to calculate average temperature for each sensor over time
SELECT
    sensor_id,
    AVG(temperature) AS avg_temperature
FROM
    sensor_data
WHERE
    timestamp >= '2023-01-01'
GROUP BY
    sensor_id;
