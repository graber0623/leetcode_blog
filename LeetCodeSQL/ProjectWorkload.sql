# Write your MySQL query statement below
with cte as(
    select
    A.employee_id, A.project_id, B.name, A.workload,
    avg(workload) over(partition by team) as team_avg_workload
    from Project A
    inner join Employees B on A.employee_id = B.employee_id
)

select
employee_id, project_id, name as employee_name, workload as project_workload
from cte
where workload > team_avg_workload
order by employee_id, project_id