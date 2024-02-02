SELECT 'Low Salary' AS CATEGORY, count(account_id) AS accounts_count
FROM ACCOUNTS 
where income < 20000
UNION
SELECT 'Average Salary' AS CATEGORY, count(account_id) AS accounts_count
FROM ACCOUNTS
where INCOME BETWEEN 20000 AND 50000
UNION
SELECT 'High Salary' AS CATEGORY, count(account_id) AS accounts_count
FROM ACCOUNTS
where INCOME > 50000