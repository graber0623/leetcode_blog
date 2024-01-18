# Write your MySQL query statement below
select
S1.user_id, sum(s1.quantity*P1.price) as spending
from Sales S1
left join Product P1 on S1.product_id = P1.product_id
group by s1.user_id
order by spending desc