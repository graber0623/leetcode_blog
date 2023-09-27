with t_1_3 as (
    SELECT *
    FROM
    (
    select 
        t.client_id,
        t.driver_id,
        t.status,
        t.request_at,
        u1.banned as userbanned,
        u2.banned as clientbanned
    from trips t
    left join Users u1 on t.client_id = u1.users_id
    left join Users u2 on t.driver_id = u2.users_id
    ) tt
    WHERE tt.request_at in ("2013-10-01","2013-10-02","2013-10-03") and tt.userbanned = "No" and tt.clientbanned = "No" 
), dc as (
    select
    t.request_at as day,
    count(*) as day_count
    from t_1_3 t
    group by t.request_at
), cc as (
    select
    t.request_at as day,
    count(*) as cancel_count
    from t_1_3 t
    WHERE t.status like "cancelled%"
    group by t.request_at
)

select
    d.Day,
    IFNULL(ROUND(c.cancel_count/d.day_count,2), 0) AS "Cancellation Rate"
from dc d
Left join cc c
on d.day=c.day
/* Write your T-SQL query statement below */
select request_at day
        ,round(sum(case when status = 'cancelled_by_driver' or status = 'cancelled_by_client' then 1 else 0 end)
         / (count(id) * 1.00),2) 'Cancellation Rate'
  from Trips t 
 where request_at between '2013-10-01' and '2013-10-03'
   and client_id in (select users_id from Users where banned = 'No')
   and driver_id in  (select users_id  from Users where banned = 'No')
group by request_at