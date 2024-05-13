/* Write your T-SQL query statement below */
SELECT
DISTINCT V1.viewer_id as id
FROM VIEWS V1
INNER JOIN VIEWS V2
ON V1.viewer_id = V2.author_id AND V1.article_id = V2.article_id
ORDER BY ID ASC