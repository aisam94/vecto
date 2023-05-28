SELECT
    DAYOFWEEK(weather_data.date),
    AVG(temperature) AS avg_temp,
    AVG(moisture_lvl) AS avg_moisture,
    AVG(weather_score) AS weather_score,
    (weather_score * avg_temp) / avg_moisture AS nutrition_value
FROM
    sensor_data
    INNER JOIN weather_data ON weather_data.date = sensor_data.date
GROUP BY
    DAYOFWEEK(weather_data.date);