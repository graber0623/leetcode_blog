# Write your MySQL query statement below
select
s.id, s.name
FROM students s
left join departments d
on s.department_id = d.id
WHERE d.name is null