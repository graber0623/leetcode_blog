# Write your MySQL query statement below

select
X.first_name, X.type, SEC_TO_TIME(X.duration) as duration_formatted
from
(
select
T2.first_name, T1.type, T1.duration,
row_number() over(partition by T1.type order by T1.duration desc) as rn
FROM Calls T1
INNER JOIN Contacts T2
on T1.contact_id = T2.id
) X
where X.rn <= 3