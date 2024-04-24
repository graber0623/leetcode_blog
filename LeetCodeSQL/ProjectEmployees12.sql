# Write your MySQL query statement below
with cte as (
select
    project_id, count(*) as cou
from Project
group by project_id
)

select
    project_id
from cte
where cou = (select max(cou) from cte)

# Write your MySQL query statement below
select
    p.project_id, round(avg(e.experience_years),2) as average_years
from Project P
inner join Employee e on p.employee_id = e.employee_id
group by p.project_id