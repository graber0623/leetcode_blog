# Write your MySQL query statement below
select
date_format(order_date, '%Y-%m') as month, count(*) as order_count, count(distinct customer_id) as customer_count
from Orders
where invoice > 20
group by date_format(order_date, '%Y-%m')