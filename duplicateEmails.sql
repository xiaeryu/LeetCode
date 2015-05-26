#########################################################################
## LeetCode Number 182 Duplicate Emails
## Problem description can be found here:
## https://leetcode.com/problems/duplicate-emails/
## MySQL query statement
#########################################################################

# Write your MySQL query statement below
SELECT Email
FROM(
    SELECT Email,count(Email) AS ct
    FROM Person
    GROUP BY Email
) T
WHERE ct > 1
