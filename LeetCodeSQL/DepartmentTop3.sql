-- # Write your MySQL query statement below

-- SELECT
--     d.name as Department,
--     ee.Employee,
--     ee.salary as Salary
-- FROM

-- (
-- select
--     departmentId,
--     name as Employee,
--     salary,
--     dense_rank() OVER(Partition by departmentId ORDER BY salary DESC) as ranks
-- from
--     Employee e
-- ) ee
-- LEFT JOIN Department d ON ee.departmentId=d.id 
-- WHERE ee.ranks <= 3


-- SELECT
--     D.name AS Department, 
--     E.name AS Employee, 
--     E.Salary
-- FROM 
--     Employee E
-- INNER JOIN 
--     Department D ON E.departmentId = D.id
-- WHERE 
--     (RANK() OVER (PARTITION BY E.departmentId ORDER BY E.salary DESC)) <= 3;

WITH RankedEmployees AS (
    SELECT
        D.name AS Department,
        E.name AS Employee,
        E.Salary,
        row_number() OVER (PARTITION BY E.departmentId ORDER BY E.salary DESC) AS SalaryRank
    FROM 
        Employee E
    INNER JOIN 
        Department D ON E.departmentId = D.id
)
SELECT
    Department,
    Employee,
    Salary
FROM 
    RankedEmployees
WHERE 
    SalaryRank <= 3;

