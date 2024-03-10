# Write your MySQL query statement below

select
max(p.name) as name,
IFNULL(sum(rest),0) as rest,
IFNULL(sum(paid),0) as paid,
IFNULL(sum(canceled),0) as canceled,
IFNULL(sum(refunded),0) as refunded
from Product P 
left join Invoice I
on I.product_id = P.product_id
group by P.product_id
order by name