# Write your MySQL query statement below


SELECT
count(T1.account_id) as accounts_count
FROM Subscriptions T1
LEFT JOIN Streams T2
ON T1.account_id = T2.account_id
WHERE (YEAR(t1.end_date) = 2021) and (YEAR(T2.stream_date) <> 2021 or T2.stream_date is Null)


-- 솔직히 문제 자체가 너무 음... 별로다
