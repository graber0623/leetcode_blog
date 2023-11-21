# Write your MySQL query statement below
with cte as (
    select *, 
    row_number() over(order by arrival_time asc) as rn
    from buses
)

select
c2.bus_id, IFNULL(count(P.passenger_id),0) as passengers_cnt 
from cte c1
Right join cte c2 on c1.rn +1 = c2.rn
left join Passengers P on P.arrival_time > IFNULL(c1.arrival_time,0) and P.arrival_time <= c2.arrival_time
group by c2.bus_id
order by c2.bus_id