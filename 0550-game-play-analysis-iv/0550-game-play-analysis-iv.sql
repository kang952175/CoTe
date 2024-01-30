SELECT ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM (
    SELECT 
    MIN(event_date) AS first_date,
    SUBSTRING_INDEX(SUBSTRING_INDEX(GROUP_CONCAT(event_date ORDER BY event_date), ',', 2), ',', -1) AS second_date
    FROM Activity 
    GROUP BY player_id
) AS event
WHERE DATEDIFF(second_date, first_date) = 1;

-- other solution 
/* SELECT ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) as fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
IN (SELECT player_id, MIN(event_date) AS first_login FROM ACTIVITY GROUP BY player_id) */