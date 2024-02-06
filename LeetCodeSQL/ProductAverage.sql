# Write your MySQL query statement below
select
u.product_id,
 ROUND((SUM(p.price * u.units)/SUM(u.units)),2) as average_price
from UnitsSold U
left join Prices P
ON u.product_id = p.product_id 
and (u.purchase_date between p.start_date and p.end_date)
group by u.product_id 