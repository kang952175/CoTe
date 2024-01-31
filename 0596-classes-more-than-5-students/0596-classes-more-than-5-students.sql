select class
from Courses
where (student, class) in (
    select student, class
    from Courses
    group by class
    having count(student) >= 5 
)