# Write your MySQL query statement below
select
transaction_id
from
(
select
transaction_id,
rank() over(partition by date(day) order by amount desc) rn
from Transactions
) XX
where rn = 1
order by transaction_id