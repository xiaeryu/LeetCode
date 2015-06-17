#########################################################################
## LeetCode Number 64 Minimum Path Sum
## Problem description can be found here:
## https://leetcode.com/problems/minimum-path-sum/
## Python script
#########################################################################

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if not grid:
            return 0
        nrow = len(grid)
        ncol = len(grid[0])
        storage = [[0 for i in range(ncol)] for j in range(nrow)]
        storage[0][0] = grid[0][0]
        for i in range(1,ncol):
            storage[0][i] = storage[0][i-1] + grid[0][i]
        for i in range(1,nrow):
            storage[i][0] = storage[i-1][0] + grid[i][0]
        
        for i in range(1,nrow):
            for j in range(1,ncol):
                storage[i][j] = min(storage[i-1][j],storage[i][j-1]) + grid[i][j]
        
        return storage[-1][-1]
