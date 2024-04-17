# Write your MySQL query statement below
-- with recursive cte 
with recursive cte as (
    select 1 as week_of_month
    union
    select week_of_month + 1 from cte where week_of_month < 4
), cte2 as (
    select c.week_of_month, m.membership 
    from cte c 
    join (
            select  'VIP' as membership 
            union
            select 'Premium' as membership
         ) m
)

select
    c2.week_of_month, c2.membership,
    IFNULL(T.total_amount, 0) as total_amount
from cte2 c2
left join
(
select
    FLOOR((DayOfMonth(p.purchase_date)-1)/7)+1 as week_of_month
    , u.membership as membership
    , sum(p.amount_spend) as total_amount
from Purchases P
inner join Users U
on p.user_id = u.user_id
where year(p.purchase_date) = 2023 
and u.membership in ('Premium', 'VIP') 
and dayofweek(p.purchase_date) = 6
group by FLOOR((DayOfMonth(p.purchase_date)-1)/7)+1, u.membership
) T
on c2.week_of_month = T.week_of_month and c2.membership = T.membership 
