# Write your MySQL query statement below

SELECT
    M.member_id, M.name,
    case when conver >= 0.80 then "Diamond"
        when conver < 0.80 and conver >= 0.50 then "Gold"
        when conver < 0.50  then "Silver"
        when conver is null then "Bronze" end as category
FROM Members M
LEFT JOIN
(
select
    member_id, (count(charged_amount)/count(*)) as conver
from Visits V
left join Purchases P on V.visit_id = P.visit_id
GROUP BY member_id
) T1
ON M.member_id = T1.member_id
order by member_id