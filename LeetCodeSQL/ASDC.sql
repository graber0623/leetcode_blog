-- SELECT DISTINCT
--     pay_month,
--     department_id,
--     CASE WHEN cma = dma THEN "same"
--         WHEN cma > dma THEN "lower"
--         ELSE "higher" END AS comparison
-- FROM
-- (
-- SELECT
--     department_id,
--     AVG(amount) OVER (PARTITION BY pay_month) as cma,
--     AVG(amount) OVER (PARTITION BY pay_month, department_id) as dma,
--     pay_month
-- FROM
-- (
-- SELECT
--     e.department_id,
--     s.amount,
--     DATE_FORMAT(s.pay_date, '%Y-%m') as pay_month
-- FROM Salary s
-- LEFT JOIN Employee e
-- ON s.employee_id = e.employee_id
-- ) a
-- )aa


with cte1 as(
    select
    date_format(pay_date, '%Y-%m') as pay_month, 
    avg(amount) as total_monthly_avg
    from Salary
    group by date_format(pay_date, '%Y-%m')
), cte2 as (
    select
    date_format(pay_date, '%Y-%m') as pay_month,
    department_id,
    avg(amount) as dept_monthly_avg
    from Salary S
    inner join Employee E
    on S.employee_id = E.employee_id
    group by date_format(pay_date, '%Y-%m'), e.department_id
)

select
c2.pay_month, c2.department_id, 
case when c2.dept_monthly_avg > c1.total_monthly_avg then 'higher'
    when c2.dept_monthly_avg = c1.total_monthly_avg then 'same'
    else 'lower' end as comparison
from cte2 c2
inner join cte1 c1
on c2.pay_month = c1.pay_month
order by pay_month, department_id

