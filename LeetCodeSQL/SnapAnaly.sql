select

A2.age_bucket,

IFNULL(ROUND((sum(case
when activity_type='send'
then time_spent end)/sum(time_spent))*100,2),0)
as send_perc,

IFNULL(ROUND((sum(case
when activity_type='open'
then time_spent end)/sum(time_spent))*100,2),0)
as open_perc

from Activities A1

left join Age A2

on A1.user_id 
= A2.user_id

group by A2.age_bucket