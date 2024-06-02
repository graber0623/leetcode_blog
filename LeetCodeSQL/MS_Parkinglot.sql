/* Write your T-SQL query statement below */

SELECT
car_id,
sum(fee_paid) as total_fee_paid,
sum(exit_time - entry_time) / sum(fee_paid) as 
FROM PARKINGTRANSACTIONS T1
GROUP BY car_id