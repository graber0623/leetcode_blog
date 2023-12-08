# Write your MySQL query statement below
with cte as(
    select
    spend_date, user_id, 
    case when max(platform) = min(platform) then max(platform)
        else 'both' end as platform,
    sum(amount) as total_amount
    from spending
    group by spend_date, user_id
), category as (
  select cc.spend_date , dd.platform
  from
  (select distinct(spend_date) as spend_date from Spending) cc
  join
  (
    select 'desktop' as platform
    union
    select 'mobile' as platform
    union
    select 'both' as platform
  ) DD
)

select 
  c.spend_date, c.platform, IFNULL(X.total_amount, 0) as total_amount, IFNULL(X.total_users, 0) as total_users
from category c
left join
(
select spend_date, platform, sum(total_amount) as total_amount, count(user_id) as total_users
from cte
group by spend_date, platform
) X
on  c.spend_date = X.spend_date and c.platform = x.platform