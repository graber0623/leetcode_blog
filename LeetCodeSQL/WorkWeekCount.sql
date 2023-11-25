
select
    sum(case when weekday(submit_date)>= 5 then 1 else 0 end) as weekend_cnt,
    sum(case when weekday(submit_Date)<5 then 1 else 0 end) as working_cnt
from Tasks