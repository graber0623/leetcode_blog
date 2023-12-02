with cte as
(select *,
    row_number() over (partition by player_id order by match_day) ck1,
    row_number() over (partition by player_id, result order by match_day) ck2
    FROM Matches)

# SELECT player_id, 
#     COUNT(match_day) streak
# FROM cte
# WHERE result = 'Win'
# GROUP BY 1, ck1-ck2

select * from cte

WITH cte AS
(SELECT *,
    ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_day) ck1,
    ROW_NUMBER() OVER (PARTITION BY player_id, result ORDER BY match_day) ck2
FROM Matches)

SELECT m.player_id, IFNULL(MAX(streak), 0) longest_streak
FROM 
(SELECT DISTINCT player_id FROM Matches) m 
LEFT JOIN
(SELECT player_id, 
    COUNT(match_day) streak
FROM cte
WHERE result = 'Win'
GROUP BY 1, ck1-ck2) t
ON m.player_id = t.player_id
GROUP BY 1