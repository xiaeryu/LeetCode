# Write your MySQL query statement below
SELECT Email
FROM(
    SELECT Email,count(Email) AS ct
    FROM Person
    GROUP BY Email
) T
WHERE ct > 1
