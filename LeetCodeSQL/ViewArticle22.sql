select
distinct viewer_id as id
from Views
group by view_date, viewer_id
having count(distinct article_id) >= 2
order by id asc