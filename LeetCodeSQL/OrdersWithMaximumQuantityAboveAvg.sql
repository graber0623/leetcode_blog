# Write your MySQL query statement below
with maxq as (
select
    max(avgq) as maxq
FROM
(select
    avg(quantity) as avgq
from OrdersDetails
group by order_id) XX
)

select
    order_id
from OrdersDetails
Group by order_id
having max(quantity) > (select maxq from maxq)