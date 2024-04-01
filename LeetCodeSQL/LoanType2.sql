# Write your MySQL query statement below

select
user_id
from Loans
group by user_id
having group_concat(loan_type) like '%Refinance%'
and group_concat(loan_type) like '%Mortgage%'
order by user_id