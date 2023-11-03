SELECT
    f.first_col, s.second_col
FROM (SELECT first_col, row_number() over(order by first_col asc) as rn from data) f
JOIN (select second_col, row_number() over(order by second_col desc) as rn from data) s ON f.rn = s.rn