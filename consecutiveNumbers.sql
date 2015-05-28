#########################################################################
## LeetCode Number 180 Consecutive Numbers
## Problem description can be found here:
## https://leetcode.com/problems/consecutive-numbers/
## MySQL query statement
#########################################################################

# Write your MySQL query statement below
SELECT DISTINCT L3.Num
From Logs L3, (
    SELECT L2.Id, L2.Num
    FROM Logs L1, Logs L2
    WHERE L2.Num = L1.Num
    AND L2.Id - L1.Id = 1
) L4
WHERE L3.Num = L4.Num
AND L3.Id - L4.Id = 1
