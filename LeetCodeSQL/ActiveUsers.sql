# Write your MySQL query statement below


SELECT
    DISTINCT L0.id, A.name
FROM Logins L0 
LEFT JOIN Logins L1 ON L0.id = L1.id and DATEDIFF(L1.login_date, L0.login_date) = 1
LEFT JOIN Logins L2 ON L0.id = L2.id and DATEDIFF(L2.login_date, L0.login_date) = 2
LEFT JOIN Logins L3 ON L0.id = L3.id and DATEDIFF(L3.login_date, L0.login_date) = 3
LEFT JOIN Logins L4 ON L0.id = L4.id and DATEDIFF(L4.login_date, L0.login_date) = 4
LEFT JOIN Accounts A on L0.id = A.id
WHERE L0.login_date IS NOT NULL
and L1.login_date IS NOT NULL
and L2.login_date IS NOT NULL
and L3.login_date IS NOT NULL
and L4.login_date IS NOT NULL 
ORDER BY L0.id asc