# Write your MySQL query statement below



SELECT date_id, make_name, COUNT(DISTINCT(lead_id)) AS unique_leads, COUNT(DISTINCT(partner_id)) AS unique_partners

FROM DailySales

GROUP BY date_id, make_name

/* Write your T-SQL query statement below */
SELECT
T1.date_id, T1.make_name,
count(DISTINCT T1.lead_id) as unique_leads,
count(DISTINCT T1.partner_id) as unique_partners
FROM DailySales T1
GROUP BY T1.date_id, T1.make_name