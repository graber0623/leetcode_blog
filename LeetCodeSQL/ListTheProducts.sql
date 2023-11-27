# Write your MySQL query statement below

SELECT
    P.product_name, O.unit
FROM PRODUCTS P
INNER JOIN
(
select
    product_id, sum(unit) as unit
from orders
where year(order_date) = 2020 and month(order_date) = 2
GROUP BY Product_id
HAVING SUM(UNIT) >= 100
) O
ON P.product_id = O.product_id