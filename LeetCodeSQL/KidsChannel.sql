SELECT
    C.title
FROM TVProgram T
INNER JOIN Content C
on T.content_id = C.content_id
WHERE YEAR(T.program_date) = 2020 and MONTH(T.program_date) = 6 and C.kids_content='Y'