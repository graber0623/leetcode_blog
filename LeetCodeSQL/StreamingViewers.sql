-- # Write your MySQL query statement below
-- with cte as(
-- select
-- user_id, session_type, 
-- row_number() over(partition by user_id order by session_end asc) as rn
-- from Sessions
-- )

-- select
-- c1.user_id, SUM(session_type = 'Streamer') AS sessions_count
-- from cte c1
-- inner join (select user_id from cte where rn = 1 and session_type = 'Viewer') c2
-- on c1.user_id =c2.user_id
-- group by c1.user_id
-- HAVING COUNT(DISTINCT session_type) = 2 
-- order by sessions_count desc, user_id desc

WITH cte AS (
	SELECT user_id, session_type, 
        RANK () OVER (PARTITION BY user_id ORDER BY session_start) AS rnk
    FROM Sessions
)

SELECT user_id, SUM(session_type = 'Streamer') AS sessions_count
FROM Sessions
WHERE user_id IN (
    SELECT user_id
    FROM cte 
    WHERE rnk = 1 AND session_type = 'Viewer'
)
GROUP BY user_id
HAVING COUNT(DISTINCT session_type) = 2 
ORDER BY 2 DESC, 1 DESC