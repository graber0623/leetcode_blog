SELECT
    T1.customer_id AS customer_id,
    T1.transaction_date AS consecutive_start,
    T3.transaction_date AS consecutive_end
FROM
    Transactions T1
JOIN
    Transactions T2 ON T1.customer_id = T2.customer_id 
    AND DATE_ADD(T1.transaction_date, INTERVAL 1 DAY) = T2.transaction_date 
    AND T1.amount < T2.amount
JOIN
    Transactions T3 ON T1.customer_id = T3.customer_id 
    AND DATE_ADD(T2.transaction_date, INTERVAL 1 DAY) = T3.transaction_date 
    AND T2.amount < T3.amount
WHERE
    T1.transaction_date = DATE_ADD(T3.transaction_date, INTERVAL -2 DAY);
