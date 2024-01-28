# Write your MySQL query statement below
with cte as (
    select
    user_id, visit_date, 
    rank() over(partition by user_id order by visit_date) as rn
    from UserVisits
)

select
c1.user_id, max(IFNULL(c2.visit_date,'2021-01-01')-c1.visit_date) as biggest_window
from cte c1
left join cte c2 on c1.user_id = c2.user_id and c1.rn = c2.rn - 1
#where c2.visit_date is not null
group by c1.user_id