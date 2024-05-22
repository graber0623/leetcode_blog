/* Write your T-SQL query statement below */

SELECT
max(T1.dept_name) as dept_name,
IFNULL(count(T2.student_id),0) as student_number
FROM Department T1
INNER JOIN Student T2
ON T1.dept_id = T2.dept_id
GROUP BY T1.dept_name