# Write your MySQL query statement below
WITH second_order AS(
SELECT seller_id, item_id
FROM
(
SELECT
    seller_id, item_id,
    row_number() over(partition by seller_id order by item_count desc) as rn
FROM
(
select
seller_id, item_id, count(*) as item_count
from Orders
where year(order_date) = 2019
group by seller_id, item_id
) O
) OO
WHERE OO.rn = 2
)

SELECT
    U.user_id AS seller_id,
    CASE WHEN U.favorite_brand = I.item_brand THEN "yes"
        ELSE "no" end as 2nd_item_fav_brand
FROM (SELECT * FROM Users WHERE YEAR(join_date) = 2019) U
LEFT JOIN second_order S ON U.user_id = S.seller_id 
LEFT JOIN Items I ON S.item_id = I.Item_id

