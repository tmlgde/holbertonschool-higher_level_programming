-- number of records with the same value in second_table
SELECT score, COUNT(*) AS number
from second_table
GROUP BY score
ORDER BY number DESC;
