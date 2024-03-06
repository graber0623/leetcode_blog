# Write your MySQL query statement below
select 
SUBSTRING_INDEX(email,'@',-1) as email_domain, count(*) as count
FROM emails
where email like "%.com"
group by SUBSTRING_INDEX(email,'@',-1)
order by count desc