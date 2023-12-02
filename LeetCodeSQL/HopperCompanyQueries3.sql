# Write your MySQL query statement below
with recursive month as (
    select 1 as month
    union 
    select month +1 as month from month where month < 12
)
, cte as (
select 
    XX.month, sum(ride_distance) as dist, sum(ride_duration) as dur, count(*) as cn
FROM
(
SELECT
    A.ride_id, A.ride_distance, A.ride_duration, MONTH(R.requested_at) as month
FROM AcceptedRides A
LEFT JOIN Rides R ON A.ride_id = R.ride_id
WHERE YEAR(R.requested_at) = 2020
)XX
GROUP BY XX.month
)
, cte2 as(
    select
    m.month
    ,IFNULL(dist, 0) as dist
    ,IFNULL(dur, 0) as dur
    ,IFNULL(cn, 0) as cn
    from month m
    left join cte c on m.month = c.month
)



select 
    c1.month
    , IFNULL(ROUND((c1.dist + c2.dist + c3.dist )/(3), 2),0) as average_ride_distance
    , IFNULL(ROUND((c1.dur + c2.dur + c3.dur )/(3), 2),0) as average_ride_duration
from cte2 c1
inner join cte2 c2 on c1.month = c2.month - 1
inner join cte2 c3 on c2.month = c3.month - 1
where c2.cn is not null and c3.cn is not null
order by c1.month