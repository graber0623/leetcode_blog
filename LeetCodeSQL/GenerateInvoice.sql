-- # Write your MySQL query statement below


-- # SELECT
-- #     invoice_id, sum(p1.quantity *p2.price) as price,
-- #     row_number() over(order by sum(p1.quantity *p2.price) DESC, invoice_id ASC) as rn
-- # FROM Purchases P1
-- # LEFT JOIN Products P2
-- # On P1.product_id = p2.product_id
-- # GROUP BY P1.invoice_id
-- SELECT
--     T1.product_id, T1.quantity, T1.quantity*t2.price as price
-- FROM Purchases T1
-- LEFT JOIN Products T2 On T1.product_id = T2.product_id
-- WHERE T1.invoice_id in(
-- SELECT invoice_id FROM(
-- SELECT
--     invoice_id, sum(p1.quantity *p2.price) as price,
--     row_number() over(order by sum(p1.quantity *p2.price) DESC, invoice_id ASC) as rn
-- FROM Purchases P1
-- LEFT JOIN Products P2
-- On P1.product_id = p2.product_id
-- GROUP BY P1.invoice_id) XX WHERE rn = 1
-- ) 
with cte as (
select
T1.invoice_id, T1.product_id, T1.quantity, T2.price
from Purchases T1
inner join Products T2 on T1.product_id = T2.product_id
)