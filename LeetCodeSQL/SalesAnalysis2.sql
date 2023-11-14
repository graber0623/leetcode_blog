# Write your MySQL query statement below

select
buyer_id
FROM (
select
buyer_id, MAX(p1.product_name) as s8, MAX(p2.product_name) as iPhone
from sales s
left join (SELECT * FROM product WHERE product_name = 'S8') p1 on s.product_id = p1.product_id
left join (select * from product where product_name = 'iPhone') p2 on s.product_id = p2.product_id
GROUP BY buyer_id
) X
WHERE s8 = 's8' and iphone is null