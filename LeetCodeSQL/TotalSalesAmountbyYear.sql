# Write your MySQL query statement below
with recursive cte as(
    select 
        product_id, period_start, period_end, average_daily_sales, period_start as da
    from Sales
        union all 
    select    
    product_id, period_start, period_end, average_daily_sales, date_add(da, interval 1 day) as da
    from cte
    where da < period_end
)


SELECT
    c.product_id, p.product_name, c.report_year, c.total_amount
FROM
(
select
    product_id, 
    LEFT(da, 4) as report_year, 
    sum(average_daily_sales) as total_amount
from cte 
group by product_id, LEFT(da, 4)
) c
left join product p on c.product_id = p.product_id
order by product_id, report_year