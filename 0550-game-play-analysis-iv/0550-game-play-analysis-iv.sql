SELECT ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM (
    SELECT 
    MIN(event_date) AS first_date,
    SUBSTRING_INDEX(SUBSTRING_INDEX(GROUP_CONCAT(event_date ORDER BY event_date), ',', 2), ',', -1) AS second_date
    FROM Activity 
    GROUP BY player_id
) AS event
WHERE DATEDIFF(second_date, first_date) = 1;


