select
user_id, stream_count as sessions_count
FROM (
select 
    user_id, 
    row_number() over(partition by user_id order by session_start) as rn,
    sum(case when session_type = 'Streamer' then 1 else 0 end) over(partition by user_id) as stream_count,
    count(*) over(partition by user_id) as session_count,
    session_type                   
FROM sessions ) XX
WHERE rn = 1 and session_type = 1 and stream_count >= 1                                    
order by sessions_count desc