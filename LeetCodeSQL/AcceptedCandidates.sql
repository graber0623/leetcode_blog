# Write your MySQL query statement below
SELECT
    C.candidate_id
FROM
(select candidate_id, interview_id from Candidates where years_of_exp >= 2) C
INNER JOIN
(select interview_id, sum(score) as score from Rounds group by interview_id having sum(score) > 15) S
ON C.interview_id = S.interview_id