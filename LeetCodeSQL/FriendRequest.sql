# Write your MySQL query statement below


SELECT
    IFNULL(ROUND(sum(case when accepter_id is not null Then 1
        ELSE 0 End)/count(*), 2), 0) as accept_rate
FROM (SELECT DISTINCT sender_id, send_to_id from FriendRequest) F
LEFT OUTER JOIN (select distinct requester_id, accepter_id from RequestAccepted) R
ON F.sender_id = R.requester_id and F.send_to_id = R.accepter_id

with accepted
as
(select count(distinct requester_id,accepter_id) as nr
from RequestAccepted),

sent as
(select count(distinct sender_id,send_to_id) as na
from FriendRequest)

select coalesce(round(nr/na,2),0.00) as accept_rate
from accepted,sent