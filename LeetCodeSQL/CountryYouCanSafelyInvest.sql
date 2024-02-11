# Write your MySQL query statement below
with per as (
    select
    P.id, C.name
    from Person P
    Left Join Country C
    on P.phone_number Like concat(country_code, '%')
), cte as (
    select
    caller_id as id, duration
    from Calls
    Union All
    select
    callee_id as id, duration
    from Calls
)

SELECT
P.name as country
FROM
cte c
LEFT JOIN Per P
on C.id = P.id
group by P.name
having AVG(c.duration) > (select avg(duration) from cte)