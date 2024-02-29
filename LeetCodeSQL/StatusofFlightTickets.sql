-- # Write your MySQL query statement below

-- SELECT
--     passenger_id, 
--     case when ranking <= capacity then 'Confirmed'
--         when ranking > capacity then 'Waitlist' END AS Status 
-- FROM
-- (
-- select
--     P.passenger_id, 
--     P.flight_id,
--     rank() over (partition by P.flight_id order by P.booking_time asc) as ranking,
--     F.capacity
-- from
--     Passengers P
-- left join Flights F on P.flight_id = F.flight_id
-- ) aa

-- ORDER BY passenger_id ASC
select
    passenger_id,
    case when rn <= capacity then 'Confirmed' else 'Waitlist' end as capacity
from(
select
p.passenger_id, 
F.capacity,
row_number() over(partition by p.flight_id order by booking_time asc) as rn
from Passengers P
inner join flights F on P.flight_id = F.flight_id
) XX
order by passenger_id


