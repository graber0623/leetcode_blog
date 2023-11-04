# Write your MySQL query statement below
with cte as(
SELECT
    activity, count(*) as ac_count
FROM friends GROUP BY activity
)

SELECT
    a.name as activity -- IFNULL(c.ac_count, 0) as ac_count
FROM
    Activities a
LEFT JOIN cte c ON a.name = c.activity
WHERE ac_count <> (select max(ac_count) from cte) and ac_count <>(select min(ac_count) from cte)