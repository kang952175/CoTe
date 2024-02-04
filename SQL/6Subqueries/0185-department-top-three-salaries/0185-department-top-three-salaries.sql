with Employee_with_rank as (
    select *, dense_rank() over(partition by departmentId order by salary desc) as top
    from Employee 
)

select d.name as Department,
e.name as Employee,
e.Salary
from Employee_with_rank e
left join Department d
on e.departmentId = d.id
where top < 4
order by e.top