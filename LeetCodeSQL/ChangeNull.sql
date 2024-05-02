
with recursive cte1
as (

    select id, drink, rn 
from (select id, drink, 
row_number() over() 
as rn from CoffeeShop) cte

    where rn 
= 1

    union 
all

    select cte.id, 
ifnull(cte.drink, cte1.drink), cte.rn

    from cte1

    join (select id, drink,
row_number() over ()
as rn from coffeeshop) cte

    on cte.rn 
- 1 = cte1.rn

)



select id, drink 
from cte1