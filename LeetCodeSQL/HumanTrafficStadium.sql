
with cte as(
select
s1.id id1, s2.id id2, s3.id id3,
s1.visit_date vd1, s2.visit_date vd2, s3.visit_date as vd3,
s1.people as p1, s2.people as p2, s3.people as p3
from stadium s1
left join stadium s2 on s1.id = s2.id - 1
left join stadium s3 on s1.id = s3.id - 2
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100
and s2.visit_date is not null and s3.visit_date is not null
)

select *
from
(
select 
id1 as id, vd1 as visit_date, p1 as people
from cte 
union
select 
id2 as id, vd2 as visit_date, p2 as people
from cte
union
select 
id3 as id, vd3 as visit_date, p3 as people
from cte
)XX order by id