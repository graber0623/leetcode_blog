# Write your MySQL query statement below
WITH RECURSIVE CTE AS (
    SELECT task_id, subtasks_count
    FROM Tasks
    UNION ALL
    SELECT task_id, subtasks_count - 1
    FROM CTE
    WHERE subtasks_count > 1
)

SELECT c.task_id, c.subtasks_count as subtask_id
FROM CTE c
LEFT JOIN Executed e on c.task_id = e.task_id and c.subtasks_count = e.subtask_id
WHERE e.subtask_id is Null