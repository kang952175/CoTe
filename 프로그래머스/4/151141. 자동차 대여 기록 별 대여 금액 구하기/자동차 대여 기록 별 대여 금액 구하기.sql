WITH rental_duration AS (
    SELECT 
        h.history_id,
        c.car_id,
        c.daily_fee,
        DATEDIFF(h.end_date, h.start_date) + 1 AS rental_days,
        c.car_type
    FROM 
        CAR_RENTAL_COMPANY_CAR c
    JOIN 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY h ON c.car_id = h.car_id
    WHERE 
        c.car_type = '트럭'
), discount_applied AS (
    SELECT 
        rd.history_id,
        rd.daily_fee * rd.rental_days * (1 - IFNULL(dp.discount_rate, 0) / 100) AS fee
    FROM 
        rental_duration rd
    LEFT JOIN 
        CAR_RENTAL_COMPANY_DISCOUNT_PLAN dp ON rd.car_type = dp.car_type
        AND (
            (rd.rental_days >= 90 AND dp.duration_type = '90일 이상')
            OR (rd.rental_days >= 30 AND rd.rental_days < 90 AND dp.duration_type = '30일 이상')
            OR (rd.rental_days >= 7 AND rd.rental_days < 30 AND dp.duration_type = '7일 이상')
        )
)

SELECT 
    history_id,
    ROUND(fee) AS fee
FROM 
    discount_applied
ORDER BY 
    fee DESC, 
    history_id DESC;
