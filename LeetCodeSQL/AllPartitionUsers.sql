# Write your MySQL query statement below
with cte as(
select
r1.user_id as user1_id , r2.user_id as user2_id, count(*) as cn
from Relations R1
inner join Relations R2
on R1.user_id < R2.user_id and R1.follower_id = R2.follower_id
group by r1.user_id, r2.user_id
)

select
 user1_id, user2_id
from cte where cn = (select max(cn) from cte)

-- group by R1.user_id, R2.user_id