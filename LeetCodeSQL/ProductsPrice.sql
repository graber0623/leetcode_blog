# Write your MySQL query statement below
select
    product_id,
    MAX(CASE WHEN store = 'store1' then price END) as store1,
    MAX(CASE WHEN store = 'store2' then price END) as store2,
    MAX(CASE WHEN store = 'store3' then price END) as store3
from 
Products GROUP BY product_id