#########################################################################
## LeetCode Number 118 Pascal's Triangle
## Problem description can be found here:
## https://leetcode.com/problems/pascals-triangle/
## Python script
#########################################################################

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        out = [[1 for x in range(y)] for y in range(1,numRows+1)]
        if numRows<3:
            return out
        else:
            for i in range(3,numRows+1):
                for j in range(2,i):
                    out[i-1][j-1] = out[i-2][j-2] + out[i-2][j-1]
        return out
