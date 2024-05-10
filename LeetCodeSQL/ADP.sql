# Write your MySQL query statement below

select
    ad_id, 
    IFNULL(ROUND( sum(case when action = 'Clicked' then 1 else 0 end)/sum(case when action = 'Clicked' or action = 'Viewed' then 1 else 0 end), 4 ), 0 ) * 100 as ctr
from Ads
group by ad_id
order by ctr desc, ad_id asc