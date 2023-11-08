SELECT
    user_id, name, mail
FROM
    Users
WHERE
    mail REGEXP '^[A-Za-z][a-zAZ0-9_.-]*@leetcode[.]com'