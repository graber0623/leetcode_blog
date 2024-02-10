# Write your MySQL query statement below
with cte as (
    select distinct product_id from Products
)

select
c.product_id, ifnull(c1.new_price, 10) as price
from cte c
left join (
select
product_id, new_price
from(
select product_id, new_price, change_date,
row_number() over(partition by product_id order by change_date desc) as rn
from Products
where change_date <= '2019-08-16'
) XX where rn = 1
) c1 on c.product_id = c1.product_id