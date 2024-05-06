# Write your MySQL query statement below
with cte as (
select
seat_id, free,
seat_id - row_number() over(order by seat_id asc) as gap
from
cinema
where free = 1
), cte2 as 