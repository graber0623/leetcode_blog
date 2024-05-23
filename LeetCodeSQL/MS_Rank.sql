WITH RankedEmployees AS (
    SELECT
        D.name AS Department,
        E.name AS Employee,
        RANK() OVER (PARTITION BY E.departmentId ORDER BY E.salary DESC) AS rn
    FROM Employee E
    LEFT JOIN Department D ON E.departmentId = D.id
)
SELECT
    Department,
    Employee
FROM RankedEmployees
WHERE rn <= 2;
