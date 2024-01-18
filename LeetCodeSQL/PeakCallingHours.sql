# Write your MySQL query statement below
select city, peak_calling_hour, number_of_calls
from
(
select
city, hour(call_time) as peak_calling_hour, count(*) as number_of_calls,
rank() over(partition by city order by count(*) desc) as rn
From Calls
group by city, hour(call_time)
) xx
where rn = 1
order by peak_calling_hour desc, city desc