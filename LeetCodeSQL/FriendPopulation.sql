# Write your MySQL query statement below

with cte as (
select user, sum(friend_count) as friend_count
from
(
select user1 as user, count(*) as friend_count from Friends group by user1 
union all
select user2 as user, count(*) as friend_count from Friends group by user2
) x
group by user
)

select  user as user1,  ROUND(friend_count / (select count(*) from cte) * 100,2) as percentage_popularity

from cte
order by user
