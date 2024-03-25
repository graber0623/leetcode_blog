# Write your MySQL query statement below
select
 x.follower, count(*) as num
from
(
select
    distinct f1.followee, f1.follower, f2.followee as f2followee
from follow f1
inner join follow f2 on f1.follower = f2.followee
) x 
group by x.follower