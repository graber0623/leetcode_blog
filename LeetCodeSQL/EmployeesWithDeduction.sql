# Write your MySQL query statement below

# with ne as (
#     select employee_id, needed_hours * 3600 as needed_secs from employee_id 
# ),

SELECT 
  e.employee_id
FROM employees e
LEFT JOIN(
select employee_id, SUM(TIMESTAMPDIFF(SECOND, in_time, out_time)) as worked_hours
from logs
group by employee_id
) l ON e.employee_id = l.employee_id
WHERE IFNULL(l.worked_hours, 0) < e.needed_hours * 3600