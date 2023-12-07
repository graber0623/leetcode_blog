# Write your MySQL query statement below
with ex as (
  select 'Senior' as experience
  union all
  select 'Junior' as experience
)
, se as (
    select
        experience,
        70000 - sum(salary) over(order by salary asc) as budget
    from Candidates
    where experience = 'Senior'
),
ju as (
    select
    experience,
    IFNULL((select min(budget) from se where budget >= 0), 70000) - sum(salary) over(order by salary asc) as budget
    from Candidates
    where experience = 'Junior'
)

select
  ex.experience, IFNULL(cc.accepted_candidates, 0 ) as accepted_candidates
from ex
left join 
(select experience, count(*) as accepted_candidates from se where budget >= 0 group by experience
union all
select experience, count(*) as accepted_candidates from ju where budget >= 0 group by experience) cc
on ex.experience = cc.experience
