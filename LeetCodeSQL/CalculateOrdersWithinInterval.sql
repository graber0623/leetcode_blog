# Write your MySQL query statement below
SELECT
  CEIL(minute/6) as interval_no, sum(order_count) as total_orders
FROM Orders
GROUP BY CEIL(minute/6)