# Write your MySQL query statement below
SELECT ROUND(AVG(averages),4)*100 as average_daily_percent FROM
(
select action_date, sum(removed)/count(distinct post_id) as averages from
(
select
    A.user_id, A.post_id, A.action_date,
    Case When R.post_id >= 0 then 1 else 0 end as removed
from Actions A 
left join Removals R on A.post_id = R.post_id and A.action_date <= R.remove_date
where A.action = 'report' and A.extra = 'spam'
) XX
GROUP BY action_date
) XXx