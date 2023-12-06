# Write your MySQL query statement below
select
    bike_number, max(end_time) as end_time
From Bikes
Group By Bike_Number