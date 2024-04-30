SELECT
user_id, MAX(DATEDIFF(lag_date,visit_date)) as biggest_window
FROM
(
SELECT
user_id,
visit_date,
IFNULL(LEAD(visit_date) over(partition by user_id order by visit_date), '2021-01-01') as lag_date
FROM UserVisits 
) X
GROUP BY USER_ID