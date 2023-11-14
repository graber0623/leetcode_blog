# Write your MySQL query statement below
SELECT
user_id, product_id
FROM
(
SELECT
user_id, S.product_id, S.quantity * P.price as price,
rank() over(partition by user_id order by S.quantity * P.price desc) as rn
FROM (SELECT user_id, product_id, sum(quantity) as quantity FROM Sales Group BY user_id, product_id)S
LEFT JOIN Product P
ON S.product_id = P.product_id
) XX
WHERE rn = 1