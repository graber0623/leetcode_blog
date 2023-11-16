# Write your MySQL query statement below
SELECT
seller_id, num_items
FROM
(
SELECT
  O.seller_id, count(distinct(I.item_id)) as num_items,
  rank() over(order by count(distinct(I.item_id)) DESC) as rn
FROM ORDERS O
LEFT JOIN ITEMS I on O.item_id = I.item_id
LEFT JOIN USERS U on O.seller_id = U.seller_id
WHERE I.item_brand != U.favorite_brand
GROUP BY O.seller_id
)XX
WHERE rn = 1
ORDER BY seller_id asc