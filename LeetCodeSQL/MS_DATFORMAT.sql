/* Write your T-SQL query statement below */
SELECT
FORMAT(order_date, 'yyyy-MM') as month,
count(DISTINCT order_id) as order_count,
count(DISTINCT customer_id) as customer_count
FROM ORDERS
WHERE INVOICE > 20
GROUP BY FORMAT(ORDER_DATE, 'yyyy-MM')
-- HAVING sum(invoice) > 20