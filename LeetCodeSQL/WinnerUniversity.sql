# Write your MySQL query statement below
with ny as (
select count(*) as cn from NewYork where score >= 90
), ca as (
    select count(*) as cc from California where score >= 90
)


select
    CASE WHEN n.cn > c.cc then 'New York University' 
        when n.cn < c.cc then 'California University'
        else 'No Winner' end as winner
from ny n 
join ca c