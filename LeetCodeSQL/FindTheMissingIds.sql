with recursive cte as (
    select 1 as ids
    union 
    select ids +1 as ids from cte where ids < (select max(customer_id) as ids from Customers)
)

select
ids
from cte c1
left join customers c2
on c1.ids = c2.customer_id 
where c2.customer_id is null