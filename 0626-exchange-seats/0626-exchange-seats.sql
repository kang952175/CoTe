SELECT
CASE
    WHEN mod(id, 2) != 0 AND counts != id THEN id + 1
    WHEN mod(id, 2) != 0 AND counts = id THEN id
    ELSE id - 1
END AS id,
student
FROM
(SELECT *, COUNT(*) OVER() AS counts FROM Seat) AS Seat_alias
ORDER BY id;

