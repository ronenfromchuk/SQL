select * from sp_populate_grades(5, 30);

select * from (
select *,
       row_number() over (partition by class_id order by class_id, grade desc) row_num
from grades) c
where c.row_num between 1 and 2;

select * , (grade - class_avg) diff from (
select student_id, class_id, grade,
       count(*) over (partition by class_id) students_in_class,
       avg(grade) over (partition by class_id) class_avg
from grades ) c;

select class_id, avg(grade)
from grades
group by class_id;
