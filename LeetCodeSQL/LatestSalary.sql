# Write your MySQL query statement below
select
emp_id, firstname, lastname, salary, department_id
from
(
select
*,
rank() over(partition by emp_id order by salary desc) rn
from Salary
) XX
where rn = 1