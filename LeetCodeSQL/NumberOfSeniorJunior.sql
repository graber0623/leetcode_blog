with Sen as 
(
select
employee_id,
70000-sum(salary) over(order by salary asc) as remain
from candidates
where experience = 'Senior'
)

select employee_id from sen where remain >= 0
union all
select
employee_id
from
(
select
employee_id,
(select IFNULL(min(remain),70000) from sen where remain >= 0) - sum(salary) over(order by salary asc) as remain
from Candidates
where experience = 'Junior'
) XX
where remain >=0