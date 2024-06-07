WITH CTE AS (
    SELECT 
        player_id, 
        device_id, 
        event_date,
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date ASC, device_id ASC) AS rn
    FROM 
        Activity
)
SELECT 
    player_id, 
    device_id
FROM 
    CTE
WHERE 
    rn = 1;
