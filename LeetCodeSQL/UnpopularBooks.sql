WITH order1 AS (
    select order_id, book_id, quantity
    FROM orders
    WHERE dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'
)

SELECT
    book_id,
    name
FROM
(
SELECT
    b.book_id,
    b.name,
    IFNULL(o.quantity, 0) as quantity
FROM Books b
LEFT JOIN order1 o
ON b.book_id = o.book_id
WHERE b.available_from <= "2019-05-23"
) aa
GROUP BY book_id
HAVING SUM(quantity) < 10