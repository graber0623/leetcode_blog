# Write your MySQL query statement below


with recursive cte as (
select '2020' as year, 1 as month
union all 
select year, month + 1 from cte where month < 12


), active_drivers as (
    select c.year, c.month, count(d.driver_id) as acount
    from cte c
    left join drivers d on c.year > year(d.join_date) or (c.year=year(d.join_date) and c.month >= month(d.join_date))
    group by c.year, c.month
), used_drivers as (
    select 
        year(r.requested_at) as year, month(r.requested_at) as month, count(distinct driver_id) as dcount
    from Rides R
    INNER join AcceptedRides A
    ON R.ride_id = A.ride_id
    group by year(r.requested_at), month(r.requested_at)
)

select
    a.month, IFNULL(ROUND(IFNULL(u.dcount,0)/IFNULL(a.acount,0) * 100,2),0) as working_percentage# u.dcount, a.acount
from active_drivers a
left join used_drivers u
on  a.year = u.year and a.month = u.month