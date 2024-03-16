SELECT
    city, 
    hour_call AS peak_calling_hours, 
    number_of_calls
FROM (
    SELECT
        city, 
        HOUR(call_time) AS hour_call, 
        COUNT(*) AS number_of_calls,
        RANK() OVER (PARTITION BY city ORDER BY COUNT(*) DESC) as rn
    FROM Calls
    GROUP BY city, HOUR(call_time)
) AS XX
WHERE rn = 1;
