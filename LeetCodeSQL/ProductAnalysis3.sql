# Write your MySQL query statement below
with cte as (
    select product_id, min(year) as first_year from sales group by product_id
)

select
    s.product_id, s.year as first_year, sum(quantity) as quantity, sum(price) as price
from sales s
inner join cte c
on c.product_id = s.product_id and c.first_year = s.year
group by s.product_id, s.year
# inner join Product p
# on s.product_id = p.product_id

#group by product_id, year