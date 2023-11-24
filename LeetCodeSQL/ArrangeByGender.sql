# Write your MySQL query statement below
select
user_id, gender
from
(
select
    *,
    row_number() over(partition by rn order by gender asc) as rn2
from
(
    select
        *,
        row_number() over(partition by gender order by user_id asc) as rn
    from Genders
) G
) GG