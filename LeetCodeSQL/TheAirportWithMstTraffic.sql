# Write your MySQL query statement below

with cte as (
select airport, sum(flights_count) as flights_count
from
(
select
    departure_airport as airport, flights_count
from Flights
UNION ALL
select
    arrival_airport as airport, flights_count
from Flights
)XX group by airport) 


select
    airport as airport_id
from cte
where flights_count = (select max(flights_count) from cte)