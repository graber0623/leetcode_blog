# Write your MySQL query statement below

select
    sp.salesperson_id, sp.name,  IFNULL(p.price, 0) as total
from Salesperson sp
left join
(select c.salesperson_id, IFNULL(sum(s.price),0) as price
from customer c
LEFT JOIN (SELECT customer_id, sum(price) as price from sales group by customer_id) s ON c.customer_id = s.customer_id
group by c.salesperson_id ) p on sp.salesperson_id = p.salesperson_id