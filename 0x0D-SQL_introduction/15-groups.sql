-- SELECT with COUNT and GROUP BY

SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;
