# Write your MySQL query statement belowselect*

select candidate_id
from Candidates
group by candidate_id
having group_concat(skill) like '%Python%'
and group_concat(skill) like '%Tableau%'
and group_concat(skill) like '%PostgreSQL%'