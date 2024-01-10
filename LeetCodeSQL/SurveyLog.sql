# Write your MySQL query statement below
select
    question_id as survey_log
from SurveyLog
group by question_id
# having group_concat(',',action) like "%show%" and group_concat(',',action)like '%answer%'
order by (sum(case when action = 'answer' then 1 else 0 end)/sum(case when action ='show' then 1 else 0 end) ) desc, question_id asc limit 1