with cte as (
    select customer_id, year(order_date) as year, sum(price) as total_price
    from orders
    group by customer_id, year(order_date)
), cte2 as(
select
    customer_id, 
    year, 
    total_price,
    row_number() over (partition by customer_id order by year) as rn,
    lead(year) over (partition by customer_id order by year) as next_year,
    lead(total_price) over (partition by customer_id order by year) as next_year_price
from cte
)

select
customer_id
from
(
select customer_id, next_year - year as year_diff, next_year_price - total_price as price_diff
from cte2 
where next_year is not null 
) XX 
group by customer_id 
having max(year_diff) <= 1 and min(price_diff) > 0