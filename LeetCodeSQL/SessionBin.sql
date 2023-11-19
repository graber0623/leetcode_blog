# Write your MySQL query statement below

WITH cte AS (
    SELECT '[0-5>' AS bin
    UNION ALL
    SELECT '[5-10>' AS bin
    UNION ALL
    SELECT '[10-15>' AS bin
    UNION ALL
    SELECT '15 or more' AS bin
    )

select
    bin, count(*) as total
FROM
(
select
    case when duration >= 0 and duration < 300 then '[0-5>'
        when duration >= 300 and duration < 600 then '[5-10>'
        when duration >= 600 and duration < 900 then '[10-15>'
        else '15 or more' end as bin
from Sessions
) XX
Group By bin