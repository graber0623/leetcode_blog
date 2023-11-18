with cte as (
    select
    case 
        when content like "% bull %" then 'bull'
        else null end as word1,
    case 
        when content like "% bear %" then 'bear'
        else null end as word2
from Files
)
select
    word1 as word, count(word1) as count
from cte
where word1 is not null
group by word1
union all
select
    word2 as word, count(word2) as count
from cte
where word2 is not null
group by word2 

