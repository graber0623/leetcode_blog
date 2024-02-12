# Write your MySQL query statement below
select
e.employee_id
from Employees E
left join Salaries S
on E.employee_id = S.employee_id
where s.salary is null

union

select
s.employee_id
from Salaries S
left join Employees E
on E.employee_id = S.employee_id
where e.name is null