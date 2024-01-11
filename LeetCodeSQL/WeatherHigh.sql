# Write your MySQL query statement below
# select
#     w2.id
# from Weather w1
# inner join Weather w2 on w1.recordDate +1 = w2.recordDate
# where w2.temperature > w1.temperature 

select
id
from
(
select
*, max(temperature) over(order by recordDate asc) as m
, row_number() over(order by recordDate asc) as r
from Weather
) XX
where temperature = m and r > 1