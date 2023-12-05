# Write your MySQL query statement below

# select
#     case when first_score > second_score then first_player
#         when first_score < second_score then second_player
#         when first_score == second_score 
#             and case when first_id < second_id then first_player
#         else second_player end as winner
with cte as (
select
    first_player as player_id, first_score as score
FROM Matches
union all
select
    second_player as player_id, second_score as score
from Matches
) 

select
    group_id, player_id
from (
SELECT
    P.group_id, m.player_id, sum(m.score) as score,
    row_number() over(partition by P.group_id order by sum(m.score) desc, m.player_id asc) as rn
FROM cte M
inner join Players P
ON P.player_id = M.player_id
group by P.group_id, M.player_id
) XX where rn = 1