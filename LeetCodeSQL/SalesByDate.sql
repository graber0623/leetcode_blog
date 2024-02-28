# WITH ord AS (
# SELECT 
#     order_id,
#     CASE 
#         WHEN DAYOFWEEK(order_date) = 1 THEN 'Sunday'
#         WHEN DAYOFWEEK(order_date) = 2 THEN 'Monday'
#         WHEN DAYOFWEEK(order_date) = 3 THEN 'Tuesday'
#         WHEN DAYOFWEEK(order_date) = 4 THEN 'Wednesday'
#         WHEN DAYOFWEEK(order_date) = 5 THEN 'Thursday'
#         WHEN DAYOFWEEK(order_date) = 6 THEN 'Friday'
#         WHEN DAYOFWEEK(order_date) = 7 THEN 'Saturday'
#     END AS weekday,
#     item_id,
#     quantity
# FROM Orders
# ), new_ord AS (
#   SELECT
#   item_id
#   ,sum(CASE when weekday = 'Monday' THEN quantity ELSE 0 END) AS 'Monday'
#   ,sum(CASE when weekday = 'Tuesday' THEN quantity ELSE 0 END) AS 'Tuesday'
#   ,sum(CASE when weekday = 'Wednesday' THEN quantity ELSE 0 END) AS 'Wednesday'
#   ,sum(CASE when weekday = 'Thursday' THEN quantity ELSE 0 END) AS 'Thursday'
#   ,sum(CASE when weekday = 'Friday' THEN quantity ELSE 0 END) AS 'Friday'
#   ,sum(CASE when weekday = 'Saturday' THEN quantity ELSE 0 END) AS 'Saturday'
#   ,sum(CASE when weekday = 'Sunday' THEN quantity ELSE 0 END) AS 'Sunday'
#   FROM ord
#   GROUP BY item_id
# )

# SELECT

#   category,
#   SUM(Monday) AS Monday,
#   SUM(Tuesday) AS Tuesday,
#   SUM(Wednesday) AS Wednesday,
#   SUM(Thursday) AS Thursday,
#   SUM(Friday) AS Friday,
#   SUM(Saturday) AS Saturday,
#   SUM(Sunday) AS Sunday

# FROM
# (

# SELECT
#   i.item_category as category,
#   IFNULL(o.Monday , 0) AS Monday,
#   IFNULL(o.Tuesday , 0) AS Tuesday,
#   IFNULL(o.Wednesday , 0) AS Wednesday,
#   IFNULL(o.Thursday , 0) AS Thursday,
#   IFNULL(o.Friday , 0) AS Friday,
#   IFNULL(o.Saturday , 0) AS Saturday,
#   IFNULL(o.Sunday , 0) AS Sunday
# FROM items i
# LEFT JOIN new_ord o ON i.item_id = o.item_id
# ) aa
# GROUP BY category ORDER BY category


-- SELECT i.item_category AS Category,
--     SUM(CASE WHEN DAYOFWEEK(o.order_date) = 2 THEN quantity ELSE 0 END) AS Monday,
--     SUM(CASE WHEN DAYOFWEEK(o.order_date) = 3 THEN quantity ELSE 0 END) AS Tuesday,
--     SUM(CASE WHEN DAYOFWEEK(o.order_date) = 4 THEN quantity ELSE 0 END) AS Wednesday,
--     SUM(CASE WHEN DAYOFWEEK(o.order_date) = 5 THEN quantity ELSE 0 END) AS Thursday,
--     SUM(CASE WHEN DAYOFWEEK(o.order_date) = 6 THEN quantity ELSE 0 END) AS Friday,
--     SUM(CASE WHEN DAYOFWEEK(o.order_date) = 7 THEN quantity ELSE 0 END) AS Saturday,
--     SUM(CASE WHEN DAYOFWEEK(o.order_date) = 1 THEN quantity ELSE 0 END) AS Sunday
-- FROM Items i
-- LEFT JOIN Orders o
-- ON i.item_id = o.item_id
-- GROUP BY i.item_category
-- ORDER BY i.item_category;

select
i.item_category as Category,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 2 THEN quantity ELSE 0 END) AS Monday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 3 THEN quantity ELSE 0 END) AS Tuesday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 4 THEN quantity ELSE 0 END) AS Wednesday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 5 THEN quantity ELSE 0 END) AS Thursday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 6 THEN quantity ELSE 0 END) AS Friday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 7 THEN quantity ELSE 0 END) AS Saturday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 1 THEN quantity ELSE 0 END) AS Sunday

from Orders O
inner join Items I 
on O.item_id = I.item_id
group by i.item_category