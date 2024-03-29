with friends_count AS ((SELECT requester_id AS id, COUNT(requester_id) AS count
    FROM RequestAccepted
    GROUP BY requester_id)
UNION ALL
(SELECT accepter_id AS id, COUNT(accepter_id) AS count
    FROM RequestAccepted
    GROUP BY accepter_id))

SELECT id, SUM(count) AS num
FROM friends_count
GROUP BY id
ORDER BY num DESC
LIMIT 1
