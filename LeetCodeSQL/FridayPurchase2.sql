# Write your MySQL query statement below
with recursive cte as (
    select CAST('2023-11-01' as date) as purchase_date
    union 
    select purchase_date + 1 as purchase_date 
    from cte where month(purchase_date) = 11
)


select 
week(c.purchase_date) - week('2023-11-01') + 1 as week_of_month, 
c.purchase_date,
ifnull(p.total_amount, 0) as total_amount
from cte c
left join
(
select
week(purchase_date) - week('2023-11-01') +1 as week_of_month,
purchase_date,
sum(amount_spend) as total_amount
from Purchases
where dayofweek(purchase_date) = 6
group by purchase_date
) p 
on c.purchase_date = p.purchase_date
where dayofweek(c.purchase_date) = 6
