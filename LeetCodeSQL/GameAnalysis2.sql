select player_id, device_id
from
(
select
*,
row_number() over(partition by player_id order by event_date asc) as rn
FROM Activity
) XX
where rn=1