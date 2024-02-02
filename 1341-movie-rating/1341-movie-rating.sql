(SELECT name AS results
FROM Users
WHERE user_id IN (
  SELECT user_id 
  FROM MovieRating
  GROUP BY user_id
  HAVING COUNT(DISTINCT movie_id) = (
    SELECT COUNT(DISTINCT movie_id)
    FROM MovieRating
    GROUP BY user_id
    ORDER BY COUNT(DISTINCT movie_id) DESC
    LIMIT 1)
  )
ORDER BY name
LIMIT 1)
UNION ALL
(SELECT title AS results
FROM Movies
WHERE movie_id IN (
  SELECT movie_id
  FROM MovieRating
  WHERE MONTH(created_at) = 2 AND YEAR(created_at) = 2020
  GROUP BY movie_id
  HAVING AVG(rating) = (
    SELECT AVG(rating)
    FROM MovieRating
    WHERE MONTH(created_at) = 2 AND YEAR(created_at) = 2020
    GROUP BY movie_id
    ORDER BY AVG(rating) DESC
    LIMIT 1)
  )
ORDER BY title
LIMIT 1);
