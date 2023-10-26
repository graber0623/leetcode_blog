# Write your MySQL query statement below


SELECT
S.user_id, ROUND(IFNULL(confirmation_rate, 0),2) as confirmation_rate
FROM Signups S
LEFT JOIN 
(
SELECT
    user_id,
    SUM(case when action = 'timeout' then 0 else 1 end) / count(*) as confirmation_rate
FROM Confirmations
GROUP BY user_id
) C
ON S.user_id = C.user_id