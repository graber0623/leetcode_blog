# Write your MySQL query statement below

# select
#     account_id,
#     day,
#     sum(amount) over(partition by account_id order by day asc) as balance
# from
# (select
#     account_id, day, 
#     case when type = 'Withdraw' then -1 * amount
#     else amount end as amount
# from Transactions) T1


select
    account_id,
    day,
    sum(case when type = 'Withdraw' then -1 * amount
    else amount end) over(partition by account_id order by day asc) as balance
from Transactions