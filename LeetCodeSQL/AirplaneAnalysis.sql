
# Write your MySQL query statement below


select
    F.flight_id,
    CASE WHEN IFNULL(p.tc, 0) >= F.capacity then F.capacity
    else IFNULL(p.tc, 0) end as booked_cnt,
    Case WHEN IFNULL(P.tc, 0) - F.capacity > 0 then IFNULL(P.tc, 0) - F.capacity 
    else 0 end as waitlist_cnt 
from Flights F
left join (select flight_id, count(*) as tc from Passengers group by flight_id) P
on F.flight_id = P.flight_id 
ORDER BY F.flight_id