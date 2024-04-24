# Write your MySQL query statement below
with cte as (
    select distinct driver_id from rides
)

select
    A.driver_id , IFNULL(B.cnt,0) as cnt
from cte A
left join(  
            select passenger_id as driver_id, count(*) as cnt
            from rides
            where passenger_id in (select driver_id from cte)
            group by passenger_id ) B
on A.driver_id = B.driver_id
