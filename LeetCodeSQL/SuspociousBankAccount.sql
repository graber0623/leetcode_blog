# # Write your MySQL query statement below


# SELECT
#     monthly.account_id, year, month, month_income,
#     row_number() over(partition by account_id, year order by month asc) as consecutive,
#     a.max_income
# FROM
# (
# SELECT
#     account_id, YEAR(day) as year, MONTH(day) as month, SUM(amount) as month_income
# FROM Transactions 
# WHERE type = 'Creditor'
# GROUP BY account_id, YEAR(day), MONTH(day)
# ) Monthly
# LEFT JOIN Accounts a on Monthly.account_id = a.account_id

WITH totalTransactions AS
(
SELECT
    T.account_id,
    month(day) as month,
    A.max_income
FROM Transactions T
JOIN Accounts A
    ON T.account_id = A.account_id
GROUP BY 1,2
HAVING SUM(CASE WHEN type = 'Creditor' THEN amount ELSE 0 END)  > A.max_income

)

SELECT 
    DISTINCT T1.account_id 
FROM totalTransactions  T1
JOIN totalTransactions  T2
ON T1.account_id = T2.account_id AND PERIOD_DIFF(T2.month, T1.month)=1