# Write your MySQL query statement below

SELECT
    person_name
FROM
(
select
    person_name, weight, sum(weight) over(order by turn asc) as total_weight
from Queue
) a where total_weight <= 1000 order by total_weight desc limit 1