-- -- 
-- SELECT
--     p.player_id,
--     MAX(p.player_name) AS player_name,
--     COUNT(DISTINCT c.year) AS grand_slams_count
-- FROM Players p
-- LEFT JOIN Championships c ON p.player_id IN (c.Wimbledon, c.Fr_open, c.US_open, c.Au_open)
-- WHERE 
--     COALESCE(c.Wimbledon, c.Fr_open, c.US_open, c.Au_open) IS NOT NULL
-- GROUP BY p.player_id;
SELECT
    p.player_id,
    p.player_name,
    COUNT(gc.year) AS grand_slams_count
FROM Players p
LEFT JOIN (
    SELECT Wimbledon AS winner, year FROM Championships
    UNION ALL
    SELECT Fr_open, year FROM Championships
    UNION ALL
    SELECT US_open, year FROM Championships
    UNION ALL
    SELECT Au_open, year FROM Championships
) AS gc ON p.player_id = gc.winner
GROUP BY p.player_id, p.player_name
having count(gc.year) > 0
