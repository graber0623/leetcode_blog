WITH cte AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS id,
        x,
        y
    FROM Point2D
)

SELECT
    ROUND(MIN(SQRT(POWER(c1.x - c2.x, 2) + POWER(c1.y - c2.y, 2))),2) AS shortest
FROM cte c1
JOIN cte c2
ON c1.id <> c2.id;