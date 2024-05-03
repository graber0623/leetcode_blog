with CTE AS (
SELECT
YEAR(day) as year,
MONTH(day) as month,
account_id,
sum(amount) as monthly_amount

FROM Transactions T
WHERE T.type = 'Creditor'
GROUP BY YEAR(day), MONTH(day), account_id
)



SELECT
 C1.account_id
FROM CTE C1
LEFT JOIN CTE C2 ON C1.account_id = C2.account_id and C1.year = C2.year and C1.month + 1 = C2.month
LEFT JOIN Accounts A ON C.account_id = A.account_id
WHERE C1.monthly_amount > A.max_income and C2.monthly_amount > A.max_income