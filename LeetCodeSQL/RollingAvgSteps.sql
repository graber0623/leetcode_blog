# Write your MySQL query statement below

SELECT
s1.user_id, s1.steps_date, ROUND((s1.steps_count+s2.steps_count+s3.steps_count)/3,2) as rolling_average
FROM Steps s1
LEFT JOIN Steps s2 ON s1.user_id = s2.user_id and DATEDIFF(s1.steps_date,s2.steps_date) = 1
LEFT JOIN Steps s3 ON s1.user_id = s3.user_id and DATEDIFF(s1.steps_date,s3.steps_date) = 2
WHERE s2.steps_count is NOT NULL and s3.steps_count is NOT NULL
ORDER BY s1.user_id, s1.steps_date