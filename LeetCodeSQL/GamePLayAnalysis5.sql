# Write your MySQL query statement below
WITH ACT AS(
    SELECT *,
    row_number() over(partition by player_id order by event_date asc) as login_counts
    FROM Activity
)

SELECT
    first_date as install_dt, count(*) as installs,
    ROUND(sum(second) / count(*), 2) as Day1_retention
FROM
(
SELECT
    A1.player_id, A1.event_date as first_date,
    CASE WHEN DATEDIFF(A2.event_date, A1.event_date) = 1 then 1
    else 0 end as second
FROM ACT A1
LEFT JOIN (SELECT * FROM ACT WHERE login_counts = 2)  A2 ON A1.player_id = A2.player_id 
WHERE A1.login_counts = 1
) T1
GROUP BY first_date