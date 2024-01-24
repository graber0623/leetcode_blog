# Write your MySQL query statement below
select
    e1.employee_id
from Employees E1
left join Employees E2 on e1.manager_id = e2.employee_id
where e1.salary < 30000 and e1.manager_id is not null and e2.name is null
order by e1.employee_id