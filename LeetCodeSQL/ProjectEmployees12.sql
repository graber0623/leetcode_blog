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