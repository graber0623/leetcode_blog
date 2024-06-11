/* Write your T-SQL query statement below */
select 
e.user_id
from emails e
inner join (select * from texts where signup_action = 'Verified') t
on e.email_id = t.email_id and datediff(day, signup_date, action_date)= 1
order by user_id