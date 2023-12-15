# Write your MySQL query statement below
with cte as (
    select distinct user_id, song_id, day from listens
)
SELECT
   distinct user1_id, user2_id
from (
select
 f.*, l1.day
from friendship f
inner join cte l1 on  f.user1_id = l1.user_id
inner join cte l2 on  f.user2_id = l2.user_id and l1.song_id = l2.song_id 
and l1.day = l2.day
) xx
group by user1_id ,user2_id, day
having count(*) >= 3