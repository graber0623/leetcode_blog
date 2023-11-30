# Write your MySQL query statement below

with cte as (
SELECT
    employee_id, experience, salary,
    row_number() over(partition by experience order by salary) as rn,
    sum(salary) over(partition by experience order by salary) as sum_s
FROM Candidates
), Se as (
    select * from cte where experience = "Senior" and sum_s < 70000
)

select employee_id from Se
union all
select employee_id from cte 
where experience = "Junior" and sum_s < (70000 - IFNULL((select max(Se.sum_s) from Se),0))