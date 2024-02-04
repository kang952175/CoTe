WITH daily_amount AS (
  SELECT visited_on, SUM(amount) AS amount
  FROM Customer  
  GROUP BY visited_on
),
cte AS (
  SELECT *, 
    SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS sum_amount,
    COUNT(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS cnt
  FROM daily_amount
)
SELECT visited_on, amount, average_amount
FROM (
  SELECT visited_on, 
    sum_amount AS amount,
    ROUND(sum_amount / cnt, 2) AS average_amount,
    MIN(visited_on) OVER() as first 
  FROM cte) as result
WHERE visited_on >= DATE_ADD(first, INTERVAL 6 DAY)
ORDER BY visited_on ASC;
