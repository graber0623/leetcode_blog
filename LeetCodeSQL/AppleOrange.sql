SELECT SUM(apple_count) AS apple_count, SUM(orange_count) AS orange_count
FROM
(
SELECT B.box_id, B.chest_id,
 B.apple_count + IFNULL(C.apple_count, 0) AS apple_count,
 B.orange_count + IFNULL(C.orange_count,0) AS orange_count
FROM BOXES B
LEFT JOIN Chests C on B.chest_id = C.Chest_id
) T