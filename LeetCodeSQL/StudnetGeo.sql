-- # Write your MySQL query statement below
-- SELECT
--     MAX(CASE WHEN continent = 'America' THEN name END) AS America,
--     MAX(CASE WHEN continent = 'Asia' THEN name END) AS Asia,
--     MAX(CASE WHEN continent = 'Europe' THEN name END) AS Europe
-- FROM
--     (
--         SELECT 
--         *,
--         ROW_NUMBER() OVER(PARTITION BY continent ORDER BY name) AS row_id- 
--         FROM student
--     ) t
-- GROUP BY row_id

-- select 
-- max(case when name = )

select
max(case when continent = 'America' then name end) as America,
max(case when continent = 'Asia' then name end) as Asia,
max(case when continent = 'Europe' then name end) as Europe 
from
(
select
*,
row_number() over(partition by continent order by name asc) as rn
from student
) XX
group by rn