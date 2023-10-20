# Write your MySQL query statement below

with approved as (
select DATE_FORMAT(trans_date, '%Y-%m') as month,
MAX(COUNTRY) AS country,
COUNT(*) as approved_count, 
SUM(amount) as approved_amount
FROM Transactions tt WHERE state = 'approved'
GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m') 
), charge as (
select DATE_FORMAT(c.trans_date,'%Y-%m') as month, max(t.country) as country, count(t.amount) as chargeback_count,
sum(t.amount) as chargeback_amount
from chargebacks c 
left join transactions t on c.trans_id = t.id
GROUP BY country, DATE_FORMAT(c.trans_date, '%Y-%m') 
)

SELECT month, country, 
IFNULL(approved_count, 0) as approved_count, 
IFNULL(approved_amount, 0) as approved_amount,
IFNULL(chargeback_count, 0) as chargeback_count, 
IFNULL(chargeback_amount, 0) as chargeback_amount
FROM (
select ap.month, ap.country, ap.approved_count, ap.approved_amount, ch.chargeback_count, ch.chargeback_amount
from approved ap
left join charge ch on ap.month = ch.month and ap.country =ch.country
UNION
select ch2.month, ch2.country, ap2.approved_count, ap2.approved_amount, ch2.chargeback_count, ch2.chargeback_amount
from charge ch2
left join approved ap2 on ch2.month = ap2.month and ap2.country = ch2.country
)dd