SELECT DISTINCT
    pay_month,
    department_id,
    CASE WHEN cma = dma THEN "same"
        WHEN cma > dma THEN "lower"
        ELSE "higher" END AS comparison
FROM
(
SELECT
    department_id,
    AVG(amount) OVER (PARTITION BY pay_month) as cma,
    AVG(amount) OVER (PARTITION BY pay_month, department_id) as dma,
    pay_month
FROM
(
SELECT
    e.department_id,
    s.amount,
    DATE_FORMAT(s.pay_date, '%Y-%m') as pay_month
FROM Salary s
LEFT JOIN Employee e
ON s.employee_id = e.employee_id
) a
)aa