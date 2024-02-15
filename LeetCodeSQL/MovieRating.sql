# Write your MySQL query statement below
(
select
max(name) as results
from MovieRating M
left join Users U
on M.user_id = U.user_id
group by M.user_id
order by count(*) desc, max(name) asc limit 1
)
union all
(
select
max(title) as results
from MovieRating M
left join Movies U
on M.movie_id = U.movie_id
where date_format(M.created_at, '%Y-%m') = '2020-02'
group by M.movie_id
order by avg(rating) desc, max(title) asc limit 1
)