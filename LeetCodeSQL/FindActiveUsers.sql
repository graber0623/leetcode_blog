# Write your MySQL query statement below
with cte as (
    select 
    *, 
    row_number() over() as rn
    from Users
)
select
    distinct u1.user_id
from cte U1
left join cte U2
ON u1.user_id = u2.user_id 
and datediff(u2.created_at, u1.created_at) >= 0 
and datediff(u2.created_at, u1.created_at) <= 7
and u1.rn != u2.rn
WHERE u2.created_at is not null