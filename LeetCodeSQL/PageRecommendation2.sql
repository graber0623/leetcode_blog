# Write your MySQL query statement below

with cte as (
select user1_id as user_id, user2_id as friend from Friendship
union
select user2_id as user_id, user1_id as friend from Friendship
)

select
c.user_id, l2.page_id, count(l2.page_id) as friends_likes
from cte c
left join likes l1 on c.user_id = l1.user_id
inner join Likes l2 on c.friend = l2.user_id and l1.page_id != l2.page_id
group by c.user_id, l2.page_id
order by c.user_id asc, friends_likes desc, l2.page_id asc