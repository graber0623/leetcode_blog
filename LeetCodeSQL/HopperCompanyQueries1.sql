# Write your MySQL query statement below
with recursive ms as (
    select 1 as month
    union all
    select month + 1 from ms where month < 12
)


select
    t1.month, ifnull(t1.active_drivers, 0) active_drivers, ifnull(t2.accepted_rides, 0) accepted_rides
from
(
    select
        m.month, count(dd.driver_id) as active_drivers
    from ms m
    left join (select driver_id, join_date from drivers where year(join_date) <= 2020) dd  
    on  year(join_date) * 100 + month(join_date) <= 202000 + m.month
    group by m.month
) T1
left join (
    select month(requested_at) as month, count(*) as accepted_rides 
    from rides r
    inner join AcceptedRides a on r.ride_id = a.ride_id 
    where year(requested_at) = 2020
    group by month(requested_at)
) T2
on t1.month = t2.month
