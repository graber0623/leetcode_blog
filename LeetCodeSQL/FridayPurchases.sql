# Write your MySQL query statement below
select
week(purchase_date) - 
week(cast(concat(left(cast(purchase_date as char),7), '-01') as date)) + 1 as week_of_month,
purchase_date, 
sum(amount_spend) as total_amount
from Purchases
where dayofweek(purchase_date) = 6
group by purchase_date
order by week_of_month


# select week(cast(concat(left(cast(purchase_date as char),7), '-01') as date))-1
# from purchases