# Write your MySQL query statement below
select
    p1.post_id, count(distinct p2.sub_id) as number_of_comments
from
(select distinct sub_id as post_id from Submissions where parent_id is null) p1
left join (select distinct parent_id, sub_id from submissions where parent_id is not null) p2 on p1.post_id=p2.parent_id
group by p1.post_id