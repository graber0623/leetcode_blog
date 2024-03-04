# Write your MySQL query statement below

with min_prime as(

    select

    'prime_eligible' as item_type, min(square_footage) as min_footage

    from

    Inventory

    where item_type = 'prime_eligible'

), min_none as(

    select

    "not_prime" as item_type, min(square_footage) as min_footage

    from

    Inventory

    where item_type = 'not_prime'

), cte as (

    select

    item_type, floor(500000/pow((min_footage),2)) as item_count

    from min_prime

)


 

select * from cte

union all

select

item_type, floor((select pow(min_footage,2) from min_prime)*(select item_count from cte)/pow((min_footage),2)) as item_count

from min_none