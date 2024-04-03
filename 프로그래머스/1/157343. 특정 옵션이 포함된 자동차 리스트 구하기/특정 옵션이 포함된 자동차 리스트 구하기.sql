select car_id, car_type, daily_fee, options
from CAR_RENTAL_COMPANY_CAR
where OPTIONS like '%네비게이션%'
order by car_id desc