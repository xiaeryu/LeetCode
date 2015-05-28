#########################################################################
## LeetCode Number 178 Rank Scores
## Problem description can be found here:
## https://leetcode.com/problems/rank-scores/
## MySQL query statement
#########################################################################

# Write your MySQL query statement below
SELECT Score, Rank
FROM(
    SELECT Score, @curRank := @curRank + IF(@prevScore = Score, 0, 1) AS Rank, @prevScore := Score  
    FROM Scores S, (SELECT @curRank := 0) R, (SELECT @prevScore := NULL) P  
    ORDER BY Score DESC  
) T; 
