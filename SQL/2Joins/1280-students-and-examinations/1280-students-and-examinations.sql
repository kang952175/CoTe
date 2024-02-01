SELECT st.student_id,
    st.student_name,
    sb.subject_name,
    count(ex.subject_name) AS attended_exams
FROM Students AS st
CROSS JOIN Subjects AS sb
LEFT JOIN Examinations AS ex
ON st.student_id = ex.student_id AND sb.subject_name = ex.subject_name
GROUP BY st.student_id, sb.subject_name
ORDER BY st.student_id, sb.subject_name;