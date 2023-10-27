# Write your MySQL query statement below

SELECT
    ROUND((SUM(immediate)/count(*)) * 100, 2) AS immediate_percentage
FROM
(
SELECT
    customer_id,
    case when customer_pref_delivery_date = order_date then 1 else 0 end as immediate 
FROM
(
    SELECT *, rank() over(partition by customer_id order by order_date asc) as ranking FROM delivery
) X
WHERE ranking = 1
) XX