# Write your MySQL query statement below
select
    order_date,
    RounD((sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)/count(*))*100, 2) as immediate_percentage
from Delivery
Group By order_date
order by order_date asc