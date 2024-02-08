# Write your MySQL query statement below

select
max(dept_name) as dept_name, ifnull(count(student_id), 0) as student_number 
from Department D
left join Student S 
ON D.dept_id = S.dept_id
group by D.dept_id
order by student_number desc