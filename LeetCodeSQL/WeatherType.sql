# Write your MySQL query statement below
select
max(c.country_name) as country_name,
case when avg(weather_state)  <= 15 then 'Cold'
when avg(weather_state) >= 25 then 'Hot'
else 'Warn' end as 'weather_type'

from Weather W
left join Countries C on W.country_id = C.country_id
where date_format(w.day, '%Y-%m') = '2019-11'
group by w.country_id, date_format(w.day, '%Y-%M')
-- where date_format(w.day, '%Y-%M') = '2019-11'