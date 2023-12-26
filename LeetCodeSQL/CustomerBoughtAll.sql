# Write your MySQL query statement below
with cte as (
    select distinct * from Customer
), cte2 as (
    select count(*) as c from Product
)

select
 customer_id
from cte
group by customer_id
having count(*) = (select c from cte2)