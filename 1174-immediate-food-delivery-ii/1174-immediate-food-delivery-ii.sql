SELECT 
ROUND(SUM(IF(first_order_date = first_customer_pref_delivery_date,1,0)) * 100 / COUNT(*), 2) AS immediate_percentage
FROM (SELECT 
MIN(order_date) AS first_order_date,
MIN(customer_pref_delivery_date) AS first_customer_pref_delivery_date 
FROM Delivery 
GROUP BY customer_id) AS first_delivery_table;

