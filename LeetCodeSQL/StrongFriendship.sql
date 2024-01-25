# Write your MySQL query statement below
with cte as (
    select
    user1_id as u1, user2_id as u2
    from Friendship
    union
    select
    user2_id as u1, user1_id as u2
    from Friendship
)

select
 c1.user1_id  as user1_id, c1.user2_id as user2_id, count(*) as common_friend
from Friendship c1
left join cte c2 on c1.user1_id  =c2.u1
left join cte c3 on c1.user2_id = c3.u2
where c2.u2 = c3.u1
group by c1.user1_id, c1.user2_id
having count(*) >= 3