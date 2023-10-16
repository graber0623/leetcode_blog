SELECT
    TT.activity_date as login_date, count(distinct(user_id)) as user_count
FROM
(
select
    user_id,
    activity_date,
    row_number() over(partition by user_id order by activity_date ASC) AS rn
from Traffic T
WHERE T.activity = "login"
) TT
WHERE TT.rn = 1 and datediff("2019-06-30" , TT.activity_date) <= 90
GROUP BY TT.activity_date