# Write your MySQL query statement below
WITH CTE AS(
    select *
    from Posts
    where post_date between '2024-02-01' and '2024-02-28'
), CTE2 AS(
    SELECt user_id, count(*)/4 as avg_weekly_posts FROM CTE GROUP BY user_id
), CTE3 AS(
    SELECT 
    user_id,
    post_date,
    count(*) over(PARTITION BY user_id ORDER BY post_date RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW ) AS cnt
    FROM CTE
), CTE4 AS(
    SELECT
    user_id, max(cnt) as max_7day_posts
    from cte3
    group by user_id
)

select
    c2.user_id, c4.max_7day_posts, c2.avg_weekly_posts
from cte2 c2
inner join cte4 c4
on c2.user_id = c4.user_id