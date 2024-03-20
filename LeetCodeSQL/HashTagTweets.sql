# Write your MySQL query statement below
select
hashtag, count(*) as hashtag_count
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