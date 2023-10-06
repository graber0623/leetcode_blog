select u.name, u.mail
from Contests c, Users u
where u.user_id = c.gold_medal
group by u.user_id
having count(contest_id)>=3 

union 

select  u.name, u.mail
from Users u , Contests c1 , Contests c2, Contests c3
where u.user_id in  (c1.gold_medal, c1.silver_medal, c1.bronze_medal)
      and u.user_id in  (c2.gold_medal, c2.silver_medal, c2.bronze_medal)
      and u.user_id in  (c3.gold_medal, c3.silver_medal, c3.bronze_medal)
      and c1.contest_id-1 = c2.contest_id and c2.contest_id-1 = c3.contest_id