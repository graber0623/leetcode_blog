with recursive cte as (
select 1 as month
union all
select month+1 from cte where month < 12
), cte2 as (
    select
    month(R.requested_at) as month, count(*) as accepted_rides
    from AcceptedRides A
    inner join Rides R
    on A.ride_id = R.ride_id and year(R.requested_at) = 2020
    group by month(R.requested_at)
)

select
c1.month, count(*) as active_drivers, IFNULL(max(c2.accepted_rides),0) as accepted_rides
from cte c1
left join Drivers d on year(d.join_date) < 2020 or (year(d.join_Date)=2020 and c1.month >= month(d.join_date))
left join cte2 c2 on c1.month = c2.month
group by c1.month

