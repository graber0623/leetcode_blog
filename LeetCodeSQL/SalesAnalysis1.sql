WITH CTE AS (
  SELECT Seller_id, SUM(price) as price FROM Sales Group By Seller_id
)

SELECT
seller_id
FROM cte
where price = (select max(price) from cte)