# Write your MySQL query statement below


select
Department, Employee, Salary
from
(
select
d.name as Department, e.name as Employee, salary as Salary,
rank() over(partition by d.id order by e.salary desc) as rn
from Employee e
inner join Department D On e.departmentId = d.id
) XX where rn = 1