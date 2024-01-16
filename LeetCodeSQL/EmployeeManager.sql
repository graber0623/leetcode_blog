# Write your MySQL query statement below
with cte as (
    select
    count(emp_id) as ec,
    dep_id
    from Employees group by dep_id
), cte2 as(
    select
    emp_name, dep_id, position from Employees where position='Manager'
)

select
    c2.emp_name as manager_name, c1.dep_id
from cte c1
inner join cte2 c2
on c1.dep_id = c2.dep_id
where c1.ec = (select max(ec) from cte)
order by c1.dep_id