-- # Write your MySQL query statement below
-- WITH mm AS
-- (
-- SELECT
--     username, MIN(startDate)as min_startDate
-- FROM
-- (
-- SELECT
--     username, activity, startDate, endDate,
--     RANK() OVER(PARTITION BY username ORDER BY startDate DESC) ranks
-- FROM UserActivity
-- ) a

-- WHERE ranks <= 2

-- GROUP BY username
-- )

-- SELECT
--     UserActivity.username, UserActivity.activity, UserActivity.startDate, UserActivity.endDate
-- FROM UserActivity, mm

-- WHERE UserActivity.username = mm.username AND UserActivity.startDate = mm.min_startDate
select
username, activity, startDate,endDate
from
(
select
username, activity, startDate, endDate,
row_number() over(partition by username order by rn desc) as rrn
FROM
(
select
*,
row_number() over(partition by username order by startDate desc) as rn
from UserActivity
) XX
WHERE rn <= 2 
) xxx
where rrn = 1