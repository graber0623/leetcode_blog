
# Write your MySQL query statement below



select 

customer_id, max(name) 
as name

FROM

(

SELECT

o.customer_id, o.order_date, o.quantity * p.price
as spent, c.name

FROm Orders o

left join Product p
on o.product_id 
= p.product_id

left join Customers C
on o.customer_id 
= c.customer_id

where year(order_date)
= 2020 
and month(order_date) 
in (6,7)

) XX

group by customer_id

having    sum(case
when month(order_date)
= 6 
then spent else 
0 end) >= 
100 and 
sum(case 
when month(order_date)=7
then spent else
0 end) >=
100 