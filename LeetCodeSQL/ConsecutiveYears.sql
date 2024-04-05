-- # Write your MySQL query statement below
-- with cte as (
-- select product_id, year(purchase_date) as year, count(*) as c
--  from Orders group by product_id, year(purchase_date)
-- )

-- select
-- distinct c1.product_id
-- from cte c1
-- inner join cte c2 on c1.product_id = c2.product_id and c1.year = c2.year -1
-- WHERE c1.c >= 3 and c2.c >=3
with cte as (
select
product_id, year(purchase_date) as year, count(*) as c
from Orders
group by product_id, year(purchase_date)
)

select
distinct c1.product_id as product_id
from cte c1
inner join cte c2 on c1.product_id = c2.product_id and c2.year -1 = c1.year
where c1.c >= 3 and c2.c >= 3