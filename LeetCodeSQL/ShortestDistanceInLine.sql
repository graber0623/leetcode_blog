# Write your MySQL query statement below


select min(ABS(p1.x - p2.x)) as shortest
from Point P1
cross join Point p2
WHERE p1.x != p2.x