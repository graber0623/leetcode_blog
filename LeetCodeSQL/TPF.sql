# Write your MySQL query statement below

select
policy_id,
state,
fraud_score
from
(
select
*,
percent_rank() over(partition by state order by fraud_score desc) as pct
from Fraud
) XX
where pct <= 0.05
order by state asc, fraud_score desc, policy_id asc