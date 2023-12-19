# Write your MySQL query statement below
select salary as SecondHighestSalary
FROM
(
select
    salary,
    rank() over(order by salary desc) as rn
from Employee 
) XX
where rn = 2