# Write your MySQL query statement below

select
    abs(d1.msd - d2.msm) as salary_difference
from
(select max(salary) as msd from salaries where department = 'Engineering') d1,
(select max(salary) as msm from salaries where department = 'Marketing') d2