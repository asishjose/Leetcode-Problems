WITH WeatherWithLag AS (
    SELECT 
        id, 
        recordDate, 
        temperature, 
        LAG(temperature) OVER(ORDER BY recordDate) AS prev_temp,
        LAG(recordDate) OVER(ORDER BY recordDate) AS prev_date
    FROM Weather
)
SELECT id
FROM WeatherWithLag
WHERE temperature > prev_temp 
  AND recordDate - prev_date = 1;
