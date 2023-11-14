# Write your MySQL query statement below
SELECT
city_id, day, degree
FROM
(select *, rank() over(partition by city_id order by degree desc, day asc) as rn from weather) XX
where rn = 1
order by city_id