with cte as(select distinct product_id from Products)

select
c.product_id, IFNULL(x.price, 10) as price
from cte c
left join
(
select 
product_id, new_price as price, 
row_number() over(partition by product_id order by change_date desc) as rn
from Products
where change_date <= "2019-08-16"
) X on c.product_id= x.product_id and x.rn = 1