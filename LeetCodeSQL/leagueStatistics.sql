# Write your MySQL query statement below


# select
# home_team_id,
# home_team_goals,
# away_team_goals,

# select
# away_team_id,


# from Teams T
# left Join
# (SELECT home_team_id, sum(home_team_goals) as goal_for, sum(away_team_goals) as goal_against
# FROM(
# SELECT home_team_id, home_team_goals, away_team_goals,
# case when home_team_goals > away_team_goals then 3
#     when home_team_goals = away_team_goals then 1
#     else 0 end as points from Matches 
# ) h GROUP BY home_team_id) hh on T.team_id = hh.home_team_id
# left
select
    t.team_name
    , count(*) as matches_played
    , sum(case when home > away then 3 when home = away then 1 else 0 end) as points
    , sum(home) as goal_for
    , sum(away) as goal_against
    , sum(home) - sum(away) as goal_diff
FROM
(
select home_team_id, home_team_goals as home, away_team_goals as away from matches
union all
select away_team_id as home_team_id, away_team_goals as home, home_team_goals as away from matches
) g
JOIN teams t on g.home_team_id = t.team_id
group by t.team_name
order by points desc, goal_diff desc, team_name