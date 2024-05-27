/* Write your T-SQL query statement below */
with cte as (
    select event_type, AVG(occurrences) as avg_ccc
    from Events
    group by event_type
)

select
distinct business_id
from Events T1/* Write your T-SQL query statement below */
with cte as (
    select event_type, AVG(occurrences) as avg_ccc
    from Events
    group by event_type
)

select
business_id
from Events T1
left join cte T2 on T1.event_type = T2.event_type
where occurrences > T2.avg_ccc
group by business_id
having count(T2.event_type) > 1
left join cte T2 on T1.event_type = T2.event_type
where occurrences >= T2.avg_ccc