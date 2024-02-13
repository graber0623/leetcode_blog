# Write your MySQL query statement below
with cte as (
select
A.pid
from
(
select
I1.pid
from Insurance I1
inner join Insurance I2
on I1.pid != I2.pid and I1.tiv_2015 = I2.tiv_2015
group by I1.pid
) A
left join
(
select
distinct I3.pid
from Insurance I3
inner join Insurance I4
on I3.pid != I4.pid and I3.lat = I4.lat and I3.lon = I4.lon
) B
ON A.pid = B.pid
where B.pid IS NULL
)

select
ROUND(sum(tiv_2016),2) as tiv_2016
from Insurance
where pid in (select pid from cte)