
SELECT
 A.id,
 A.company,
 A.salary
FROM
(
SELECT id,
company,
salary,
row_number()OVER(PARTITION BY company ORDER BY salary ASC, id ASC) AS ranking,
count(*)over(partition by company) as count
FROM Employee
) A
WHERE A.ranking >=count/2 and A.ranking <= count/2+1
