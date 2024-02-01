select employee_id, department_id
from Employee
group by employee_id
having count(department_id) = 1
union
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y';

