#########################################################################
## LeetCode Number 70 Climbing Stairs
## Problem description can be found here:
## https://leetcode.com/problems/climbing-stairs/
## Python script
#########################################################################

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            out = [[1,1], [1,0]]
            for i in range(0,n):
                tmp = [[0,0],[0,0]]
                tmp[0][0] = out[0][0] + out[0][1]
                tmp[0][1] = out[0][0]
                tmp[1][0] = out[1][0] + out[1][1]
                tmp[1][1] = out[1][0]
                out = tmp            
            return out[0][1]
