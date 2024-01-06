# Write your MySQL query statement below

select
machine_id, ROUND(avg(processing_time),3) as processing_time
FROM
(
select
X.machine_id, X.process_id, avg(processing_time) as processing_time
FROM
(
select
A1.machine_id, A1.process_id, ABS(a1.timestamp-a2.timestamp) as processing_time
from Activity A1
inner join Activity A2 
ON A1.machine_id = A2.machine_id and A1.process_id = A2.process_id
and A1.activity_type != A2.activity_type
) X
Group by machine_id, process_id
) XX
GROUP BY Machine_id