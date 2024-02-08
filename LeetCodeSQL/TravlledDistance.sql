# Write your MySQL query statement below
select
max(name) as name, sum(distance) as travelled_distance
from Rides R
left join Users U
on R.user_id = U.id
group by user_id
order by travelled_distance desc, name