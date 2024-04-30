with recursive cte as (
    select 1 as customer_id 
    union all
    select customer_id  + 1
    from cte where customer_id  < (select max(customer_id) from customers)
)

select
c1.customer_id  as ids
from cte C1
left join Customers C2
on c1.customer_id  = c2.customer_id 
where c2.customer_name is null