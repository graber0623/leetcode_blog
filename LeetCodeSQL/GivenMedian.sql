# Write your MySQL query statement below
SELECT
    ROUND(AVG(num*1.0), 2) AS median
    FROM
(
SELECT
    *,
    SUM(frequency) OVER (ORDER BY num ASC) AS accumulated_sum,
    SUM(frequency) OVER () / 2 AS medium_index
FROM
    Numbers
) AS A
WHERE
accumulated_sum - frequency <= medium_index AND accumulated_sum >= medium_index