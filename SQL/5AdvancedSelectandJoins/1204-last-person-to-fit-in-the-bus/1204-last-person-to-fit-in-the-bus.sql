select person_name
from (
    select person_name,
    SUM(weight) over(order by turn) as total_weight
    from Queue
    order by turn) as total_table 
where total_weight <= 1000
order by total_weight desc
limit 1