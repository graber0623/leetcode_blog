# Write your MySQL query statement below

# WITH cte AS (
#     SELECT
#     *, row_number() over(partition by user_id order by purchase_date asc) as rn
#     FROM purchases
# )

# SELECT
#     user_id
# FROM
# (
# SELECT
#     c1.user_id, 
#     case 
#     when datediff(c2.purchase_date, c1.purchase_date) <= 7 then 1
#     else 0 end as tr
# FROM cte c1
# LEFT JOIN cte c2 
# ON c1.user_id = c2.user_id and c1.rn = c2.rn-1
# ) XX
# GROUP BY user_id HAVING SUM(tr) > 0 ORDER BY user_id


select distinct user_id
from (
select user_id, purchase_date,
lead(purchase_date) over (partition by user_id order by purchase_date asc) af
from purchases) a
where datediff(af,purchase_date) <= 7

-- lead 함수