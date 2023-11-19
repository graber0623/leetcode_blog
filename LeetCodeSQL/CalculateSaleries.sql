# Write your MySQL query statement below
# select
#     company_id,
#     employee_id,
#     employee_name,
#     ROUND(case when salary < 1000 then salary
#         when salary >= 1000 and salary <= 10000 then salary * 0.76
#         when salary > 10000 then salary * 0.51 end, 0) as salary
# from Salaries
with cte as (
    select
        company_id, max(salary) as max_salary
    from Salaries 
    group by company_id
)

select 
    s1.company_id,
    employee_id,
    employee_name,
    ROUND(case when s2.max_salary < 1000 then salary
        when s2.max_salary >= 1000 and s2.max_salary <= 10000 then salary * 0.76
        when s2.max_salary > 10000 then salary * 0.51 end, 0) as salary
from Salaries s1
left join cte s2
on s1.company_id = s2.company_id