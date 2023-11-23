# Write your MySQL query statement below
with cte as(
    select
        p.platform, e.experiment_name
    from
    (
        select "Android" as platform
        union all
        select "IOS" as platformm
        union all
        select "Web" as platform
    ) p
    join
    (
        select "Programming" as experiment_name
        union all
        select "Sports" as experiment_name
        union all
        select "Reading" as experiment_name
    ) e
)

select
c.platform
,c.experiment_name
, IFNULL(e.num_experiments, 0) as num_experiments
from cte c
left join 
    (
        select platform, experiment_name, count(*) as num_experiments
        from Experiments
        group by platform, experiment_name
    ) e
on c.experiment_name = e.experiment_name and c.platform = e.platform