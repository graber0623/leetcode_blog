# Write your MySQL query statement below
with cte as (
select
city, avg(price) as ap
from Listings
group by city 
)

select
city
from cte
where ap >= (select avg(ap) from cte)
order by city