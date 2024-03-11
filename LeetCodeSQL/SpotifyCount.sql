# Write your MySQL query statement below
select
artist, count(*) as occurrences
from Spotify
group by artist