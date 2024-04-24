# Write your MySQL query statement below
with cte as (
select voter, candidate, 
    ROUND(1/count(*) over(partition by voter), 2) as per 
from Votes where candidate is not null
)


select
    T1.candidate
FROM
(
select
    candidate, sum(per) as votes,
    dense_rank() over(order by sum(per) desc) as dr
from cte
group by candidate ) T1 where dr = 1 order by candidate