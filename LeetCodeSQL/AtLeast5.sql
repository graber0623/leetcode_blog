# Write your MySQL query statement below
select
    max(E2.name) as name
from Employee E1
inner join Employee E2 on E1.managerId = E2.id
GROUP BY E1.managerId
HAVING count(*) >= 5