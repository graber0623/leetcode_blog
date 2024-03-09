with recursive cte as (
    select 1 as period
    union 
    select period + 1 from cte where period < 10
)
select
period as month, round(avg(ride_distance),2) as average_ride_distance, round(avg(ride_duration),2) as average_ride_duration
from
(
select
XX.*, c.period
from
(
select
A.*, R.requested_at
from AcceptedRides A
inner join Rides R on A.ride_id = R.ride_id
where YEAR(R.requested_at) = 2020
) XX
left join cte c on c.period between month(requested_at)-2 and month(requested_at) 
) XXX
group by xxx.period