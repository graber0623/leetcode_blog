# Write your MySQL query statement below


SELECT
distinct id
FROM
(
SELECT
viewer_id as id,
count(article_id) over(partition by viewer_id, view_date) as daily_count
FROM (SELECT DISTINCT * FROM VIEWS) VV
) V
WHERE daily_count >= 2

SELECT DISTINCT viewer_id AS id
FROM Views
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) > 1
ORDER BY 1