# Write your MySQL query statement below
SELECT
X.Team_id, x.Name, (X.ori_rank - X.change_rank) as rank_diff
FROM(
SELECT
    T.team_id,
    T.name,
    CAST(rank() over(order by T.points desc, T.name asc) AS SIGNED) as ori_rank,
    CAST(rank() over(order by T.points+P.points_change DESC, T.name asc) AS SIGNED) AS change_rank
FROM TeamPoints T
LEFT JOIN PointsChange P
ON T.team_id = P.team_id
)X