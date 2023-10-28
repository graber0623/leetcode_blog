# # Write your MySQL query statement below

# with cte as (
# SELECT
#     id, drink, row_number() over() as rn
# FROM CoffeeShop
# )

# SELECT
# c1i as id, coalesce(c1d, c2d, c3d) as drink
# FROM
# (
# select
# c1.id as c1i, c1.drink as c1d, c1.rn as c1r,
# c2.id as c2i, c2.drink as c2d, c2.rn as c2r,
# c3.id as c3i, c3.drink as c3d
# from cte c1
# left join cte c2 on c1.rn = c2.rn +1 and c1.drink is null
# left join cte c3 on c1.rn = c3.rn +2 and c1.drink is null and c2.drink is null
# ) XX

WITH CTE AS (
SELECT *, row_number() over() as rn FROM CoffeeShop
)
, cte1 as (
SELECT *, count(drink) over(order by rn) as cnt from cte
)
select id, first_value(drink) over (partition by cnt) as drink from cte1
