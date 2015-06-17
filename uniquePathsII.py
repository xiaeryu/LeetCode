#########################################################################
## LeetCode Number 63 Unique Paths II 
## Problem description can be found here:
## https://leetcode.com/problems/unique-paths-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        nrow = len(obstacleGrid)
        ncol = len(obstacleGrid[0])
        storage = [[0 for i in range(ncol)] for j in range(nrow)]
        
        storage[0][0] = [1,0][obstacleGrid[0][0]]
        for i in range(1,ncol):
            if obstacleGrid[0][i] != 1 and storage[0][i-1] == 1:
                storage[0][i] = 1
        
        for i in range(1,nrow):
            if obstacleGrid[i][0] != 1 and storage[i-1][0] == 1:
                storage[i][0] = 1
        
        for i in range(1,nrow):
            for j in range(1,ncol):
                if obstacleGrid[i][j] == 1:
                    storage[i][j] = 0
                else:
                    storage[i][j] = storage[i][j-1] + storage[i-1][j]
        
        return storage[-1][-1]
