# Write your MySQL query statement below

SELECT
player_id, event_date,
sum(games_played) over(partition by player_id order by event_date asc) as games_played_so_far
FROM
(
select
player_id, event_date, sum(games_played) as games_played
from Activity 
group by player_id, event_date
) XX
