# Write your MySQL query statement below
SELECT
    employee_id, name, salary,
    dense_rank() over(order by salary asc) as team_id
FROM (
    SELECT
        employee_id,
        name,
        salary,
        count(employee_id) over(partition by salary) as team_count
    FROM
        Employees 
) E
WHERE team_count > 1
ORDER BY team_id, employee_id
