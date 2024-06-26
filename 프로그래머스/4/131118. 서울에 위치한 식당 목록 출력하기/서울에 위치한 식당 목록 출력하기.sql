SELECT R1.REST_ID, R1.REST_NAME, R1.FOOD_TYPE, R1.FAVORITES, R1.ADDRESS, ROUND(AVG(R2.REVIEW_SCORE),2) AS SCORE
FROM REST_INFO R1, REST_REVIEW R2
WHERE R1.REST_ID = R2.REST_ID AND LEFT(R1.ADDRESS, 2) = '서울'
GROUP BY R1.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC