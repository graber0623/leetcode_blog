# Write your MySQL query statement below
with av as (
select
    event_type, avg(occurences) as avg_occu
from Events
group by Event_type
)

select
    business_id
FROM Events e
left join av a
on e.event_type = a.event_type
where occurences > avg_occu
group by business_id
having count(distinct e.event_type) > 1 