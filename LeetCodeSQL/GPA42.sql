# Write your MySQL query statement below

select
    round(count(distinct t2.player_id)/count(distinct(t1.player_id)),2) as fraction
from activity t1, (
select
distinct a1.player_id
from Activity a1
inner join Activity a2
on a1.player_id = a2.player_id and a1.event_date = date_add(a2.event_date, interval -1 day)
) t2