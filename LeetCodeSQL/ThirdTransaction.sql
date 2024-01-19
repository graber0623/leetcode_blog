# Write your MySQL query statement below
with cte as(
select
user_id, spend,transaction_date,
rank() over(partition by user_id order by transaction_date asc) as rn
from Transactions
)

select
c1.user_id,
c1.spend as third_transaction_spend,
c1.transaction_date as third_transaction_date
from cte c1
left join cte c2 on c1.user_id = c2.user_id and c1.rn = c2.rn + 1
left join cte c3 on c1.user_id = c3.user_id and c1.rn = c3.rn + 2
where c1.rn = 3 and c1.spend > c2.spend and c1.spend > c3.spend
