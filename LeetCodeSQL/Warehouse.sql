# Write your MySQL query statement below
select
W.name as warehouse_name, SUM(P.Width * P.Length * P.Height *W.units) as volume
from Warehouse W
left join Products P
ON W.product_id = P.product_id
group by W.name