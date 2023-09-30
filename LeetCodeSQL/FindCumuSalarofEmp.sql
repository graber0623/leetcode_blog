# Write your MySQL query statement below
select
id,
month,
salary
FROM
(
SELECT
    e0.id,
    e0.month,
    e0.salary + IFNULL(e1.salary, 0) + IFNULL(e2.salary, 0) as salary,
    row_number() over (partition by e0.id ORDER BY e0.month DESC) as month_rank
FROM Employee e0
left join Employee e1 ON e0.id = e1.id and e0.month = e1.month +1
left join Employee e2 ON e0.id = e2.id and e0.month = e2.month +2

) a
WHERE month_rank <> 1
ORDER BY a.id ASC, a.month DESC