# Write your MySQL query statement below
select
    extra as report_reason, count(*) as report_count
from (select distinct post_id, action_date,action,extra from Actions) XX
where action_date = '2019-07-04' and action = 'report'
GROUP BY extra