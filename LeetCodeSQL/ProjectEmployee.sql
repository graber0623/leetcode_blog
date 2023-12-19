# Write your MySQL query statement below
select
project_id, employee_id
FROM
(
SELECT
p.project_id, e.employee_id,
rank() over(partition by p.project_id order by experience_years desc) as rn
FROM Project p
left join employee e on p.employee_id = e.employee_id
) XX WHERE rn = 1