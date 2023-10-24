# Write your MySQL query statement below
WITH paid AS(
    SELECT paid_by, SUM(amount) as amt FROM transactions
    GROUP BY paid_by
), received AS(
    SELECT paid_to, SUM(amount) as amt FROM transactions
    GROUP BY paid_to
)

SELECT
    user_id, user_name, 
    u.credit - IFNULL(p.amt, 0) + IFNULL(r.amt,0) as credit,
    CASE WHEN u.credit - IFNULL(p.amt, 0) + IFNULL(r.amt,0)  >= 0 THEN 'No'
        ELSE 'Yes' End as credit_limit_breached
FROM Users U
LEFT JOIN paid p on u.user_id = p.paid_by
LEFT JOIn received r on u.user_id = r.paid_to




# SELECT
    # user_id, max(user_name) as user_name, 
    # AVG(credit) - IFNULL(SUM(t1.amount), 0) + IFNULL(SUM(t2.amount),0) as credit,
    # CASE WHEN AVG(credit) - IFNULL(SUM(t1.amount), 0) + IFNULL(SUM(t2.amount),0) >= 0 THEN 'No'
    #     ELSE 'Yes' End as credit_limit_breached
# FROM Users u
# LEFT JOIN Transactions t1 ON u.user_id = t1.paid_by
# LEFT JOIN Transactions t2 ON u.user_id = t2.paid_to
# GROUP BY u.user_id