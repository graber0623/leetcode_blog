/* Write your T-SQL query statement below */
select

ROUND(cast(sum(item_count * order_occurrences) as float) / cast(sum(order_occurrences) as float), 2) as average_items_per_order

FROM Orders

-- in mssql you must cas it as float or decimal for it to become like 1.blabla when calculating int type columns