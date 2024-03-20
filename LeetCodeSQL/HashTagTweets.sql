# Write your MySQL query statement below
select
HASHTAG, count(*) as HASHTAG_COUNT
from

(
select
    SUBSTRING_INDEX(
        SUBSTRING(tweet, LOCATE('#', tweet)), 
        ' ', 
        1
    ) AS hashtag
from Tweets
) XX
group by hashtag
order by hashtag_count desc limit 3