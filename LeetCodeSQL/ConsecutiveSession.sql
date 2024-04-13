# Write your MySQL query statement below
select
distinct s1.user_id
from Sessions S1
inner join Sessions S2
on s1.user_id = s2.user_id
and s1.session_id <> s2.session_id
and s1.session_type = s2.session_type
and s1.session_end < s2.session_start
and DATE_ADD(s1.session_end, INTERVAL 12 Hour) >= s2.session_start
order by s1.user_id