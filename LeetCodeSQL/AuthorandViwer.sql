# Write your MySQL query statement below
with authors as (
select distinct author_id from Views
), no as (
select
distinct viewer_id
from views
where author_id = viewer_id
)

select 
a.author_id as id
from authors a inner join no n on a.author_id = n.viewer_id