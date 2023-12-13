# Write your MySQL query statement below
with cte as (
select
    caller_id, recipient_id, call_time, 
    row_number() over(partition by date(call_time) order by call_time asc) as rn
from Calls 
), cte2 as (
select date(call_time) as call_date, max(rn) as maxrn, min(rn) as minrn
from cte
GROUP BY date(call_time)
), cte3 as (
    select caller_id as user_id, call_time, rn from cte
    union
    select recipient_id as user_id, call_time, rn from cte
)

# select c3.*, c2.*
# from cte3 c3
select distinct user_id
from
(
select user_id, date(call_time) as call_date, max(rn) as maxrn, min(rn) as minrn
from cte3
group by user_id, date(call_time)
) c3
inner join cte2 c2 on c3.call_date = c2.call_date and c3.maxrn = c2.maxrn and c3.minrn = c2.minrn

