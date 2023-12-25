# Write your MySQL query statement below
with cte as(
    select candidateId, count(*) as cou
    from Vote
    group by candidateId
)

select
    T2.name
from cte T1
inner join candidate T2 ON T1.candidateId = T2.id  
where cou = (select max(cou) from cte)