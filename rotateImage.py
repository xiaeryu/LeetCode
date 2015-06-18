#########################################################################
## LeetCode Number 48 Rotate Image 
## Problem description can be found here:
## https://leetcode.com/problems/rotate-image/
## Python script
#########################################################################

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        matrix.reverse()
        nrow = len(matrix)
        ncol = len(matrix[0])
        for i in range(nrow):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
