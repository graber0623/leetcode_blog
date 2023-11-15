# Write your MySQL query statement below
with cte as (
    SELECT category, count(*) as accounts_count
FROM
(
select
    case when income between 20000 and 50000 then "Average Salary"
        when income > 50000 then "High Salary"
        else "Low Salary" end as category
from Accounts
) XX GROUP BY category
)

SELECT
 c1.category, IFNULL(c2.accounts_count,0) as accounts_count
FROM
(
SELECT 'High Salary' AS category
UNION ALL
SELECT 'Average Salary'
UNION ALL
SELECT 'Low Salary'
) c1
LEFT JOIN cte c2 on c1.category = c2.category
