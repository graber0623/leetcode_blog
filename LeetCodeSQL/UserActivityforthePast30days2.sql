# Write your MySQL query statement below
SELECT IFNULL(ROUND(AVG(c), 2),0) as average_sessions_per_user
FROM
(
SELECT
    user_id, count(distinct session_id) as c
FROM Activity
WHERE timestampdiff(month, activity_date, '2019-07-27') < 1
group by user_id ) XX