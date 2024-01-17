# Write your MySQL query statement below
select
e1.metal, e2.nonmetal
from (select symbol as metal from elements where type = 'metal') e1
JOIN (select symbol as nonmetal from elements where type = 'nonmetal') e2