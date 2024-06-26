WITH GRADE_INFO AS (
  SELECT
    D.ID,
    D.EMAIL,
    D.SKILL_CODE,
    CASE
      WHEN D.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') > 0 
        AND D.SKILL_CODE & (SELECT BIT_OR(CODE) FROM SKILLCODES  WHERE CATEGORY = 'Front End') !=0 THEN 'A'
      WHEN D.SKILL_CODE & (SELECT CODE FROM SKILLCODES  WHERE NAME = 'C#') > 0 THEN 'B'
      WHEN D.SKILL_CODE & (SELECT BIT_OR(CODE) FROM SKILLCODES  WHERE CATEGORY = 'Front End') !=0 THEN 'C'
      ELSE NULL
    END AS GRADE
  FROM
    DEVELOPERS D
)

SELECT GRADE,ID,EMAIL
FROM GRADE_INFO
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID