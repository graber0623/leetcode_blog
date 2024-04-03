# Write your MySQL query statement below
with RECURSIVE cte as (
    select
    substring_index(substring_index(tweet, "#", -1), " ", 1) as tag,
    substring(tweet, 1, length(tweet)-locate("#", reverse(tweet))) as remain
    from tweets
    union all
    select
    substring_index(substring_index(remain, "#", -1), " ", 1) AS tag,
    substring(remain, 1, length(remain)-locate('#', reverse(remain))) as remain
    from cte where locate("#", remain) > 0
)

select * from cte