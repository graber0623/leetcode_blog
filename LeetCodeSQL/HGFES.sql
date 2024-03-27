# Write your MySQL query statement below

SELECT
    a.student_id, a.course_id, a.grade
    
FROM
(
SELECT
    student_id, course_id, grade,
    DENSE_RANK() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id ASC) as ranks

FROM Enrollments
) a

WHERE a.ranks = 1