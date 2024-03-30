# Write your MySQL query statement below
WITH t AS
(
SELECT team_id, count(employee_id) as team_size

FROM Employee

GROUP BY team_id)


SELECT e.employee_id, t.team_size

FROM Employee e

LEFT JOIN t

on e.team_id = t.team_id