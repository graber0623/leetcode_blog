with cte as(

select
user_id1, user_id2
from Friends

union

select
user_id2 as user_id1,
user_id1 as user_id2
from Friends
) 


select 
-- c3.user_id1 as c3u1
 c1.user_id1
, c1.user_id2
-- , c2.user_id2 as c2u2
-- 
from Friends c1
left join cte c2 on c1.user_id2 = c2.user_id1 and c2.user_id2 != c1.user_id1
left join cte c3 on c1.user_id1 = c3.user_id2 and c3.user_id1 = c2.user_id2  
where c3.user_id1 is null and c2.user_id2 is null
-- select
-- c1.user_id1, c1.user_id2
-- from cte c1
-- left join cte c2 on c1.user_id2 = c2.user_id1 and c1.user_id1 != c2.user_id1 
-- where c2.user_id2 is null