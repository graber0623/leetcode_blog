# Write your MySQL query statement below
select
student_id, department_id, IFNULL(ROUND(((ranking-1) * 100 / (department_count-1)), 2),0) as percentage
from
(select
    student_id, department_id,
    rank() over(partition by department_id order by mark desc) as ranking,
    count(*) over(partition by department_id) as department_count
from students) a

SELECT student_id, department_id, 
    ROUND(100*PERCENT_RANK() OVER (
          PARTITION BY department_id 
          ORDER BY mark DESC)
    , 2) AS percentage 
FROM Students