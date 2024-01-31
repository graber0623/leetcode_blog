# Write your MySQL query statement below
select
date_format(trans_date, '%Y-%m') as month, country, count(*) as trans_count,
Count(Case When state = 'approved' then amount else null end) as approved_count,
SUM(amount) as trans_total_amount,
SUM(Case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
group by date_format(trans_date, '%Y-%m'), country