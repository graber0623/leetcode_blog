# Write your MySQL query statement below
with recursive cte2 as (
    select 0 as transactions_count
    union all
    select transactions_count + 1
    from cte2
    where transactions_count <= (select max(transactions_count) from  
                                            (select
                                            user_id, count(user_id) as transactions_count
                                            from Transactions
                                            group by user_id) XX
))

select
    c2.transactions_count, 
    IFNULL(c3.visits_count, 0) as visits_count
from cte2 c2
left join (
        select transactions_count, count(user_id) as visits_count 
        from (
            select
            user_id, count(user_id) as transactions_count
            from Transactions
            group by user_id) XX 
        group by transactions_count) c3 
on c2.transactions_count = c3.transactions_count
order by transactions_count
