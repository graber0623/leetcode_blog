# Write your MySQL query statement below
with cte as (
select
country, points, winery,
row_number() over(partition by country order by points desc) as rn
from 
(select country, sum(points) as points, winery from Wineries group by country, winery) XX
)


select
country, 
IFNULL(MAX(CASE WHEN rn = 1 then concat(winery,' (', CAST(points as char), ')') else NULL end), 'No top winery') as top_winery,
IFNULL(MAX(CASE WHEN rn = 2 then concat(winery,' (', CAST(points as char), ')') else NULL end), 'No second winery') as second_winery,
IFNULL(MAX(CASE WHEN rn = 3 then concat(winery,' (', CAST(points as char), ')') else NULL end), 'No third winery') as third_winery
from cte
group by country