-- list all records better or equal than 10

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
