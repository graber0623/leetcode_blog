-- # Write your MySQL query statement below
-- WITH RECURSIVE CTE AS (
--     SELECT task_id, subtasks_count
--     FROM Tasks
--     UNION ALL
--     SELECT task_id, subtasks_count - 1
--     FROM CTE
--     WHERE subtasks_count > 1
-- )

-- SELECT c.task_id, c.subtasks_count as subtask_id
-- FROM CTE c
-- LEFT JOIN Executed e on c.task_id = e.task_id and c.subtasks_count = e.subtask_id
-- WHERE e.subtask_id is Null

WITH RECURSIVE CTE AS(
    SELECT task_id, 1 as subtask_id from Tasks
    union all
    select c1.task_id, c1.subtask_id + 1 as subtasks_count
    from cte c1
    inner join (select task_id, subtasks_count from Tasks) c2 
    on c1.task_id = c2.task_id and c1.subtask_id < c2.subtasks_count
)

select c1.task_id, c1.subtask_id
from cte c1
left join executed c2
on c1.task_id = c2.task_id and c1.subtask_id = c2.subtask_id
where c2.subtask_id is null