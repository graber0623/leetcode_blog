# Write your MySQL query statement below
select
    id,
    MAX(CASE WHEN month = 'Jan' then revenue else Null end) as Jan_Revenue,
    MAX(CASE WHEN month = 'Feb' then revenue else Null end) as Feb_Revenue,
    MAX(CASE WHEN month = 'Mar' then revenue else Null end) as Mar_Revenue,
    MAX(CASE WHEN month = 'Apr' then revenue else Null end) as Apr_Revenue,
    MAX(CASE WHEN month = 'May' then revenue else Null end) as May_Revenue,
    MAX(CASE WHEN month = 'Jun' then revenue else Null end) as Jun_Revenue,
    MAX(CASE WHEN month = 'Jul' then revenue else Null end) as Jul_Revenue,
    MAX(CASE WHEN month = 'Aug' then revenue else Null end) as Aug_Revenue,
    MAX(CASE WHEN month = 'Sep' then revenue else Null end) as Sep_Revenue,
    MAX(CASE WHEN month = 'Oct' then revenue else Null end) as Oct_Revenue,
    MAX(CASE WHEN month = 'Nov' then revenue else Null end) as Nov_Revenue,
    MAX(CASE WHEN month = 'Dec' then revenue else Null end) as Dec_Revenue
FROM Department
GROUP BY id