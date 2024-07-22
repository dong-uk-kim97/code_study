-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS 
WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty") and 
SEX_UPON_INTAKE LIKE "Spayed%"
ORDER BY ANIMAL_ID;