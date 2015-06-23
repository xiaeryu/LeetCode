#########################################################################
## LeetCode Number 52 N-Queens II 
## Problem description can be found here:
## https://leetcode.com/problems/n-queens-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        self.n = n
        self.storage = [-1] * n
        self.output = 0
        self.column = [0] * n
        self.slope1 = [0] * (2*n-1)
        self.slope2 = [0] * (2*n-1)
        self.stepSolve(0)
        return self.output

    def stepSolve(self,i):
        for j in range(self.n):
            if (self.column[j]==0 and self.slope1[i+j]==0 and self.slope2[i-j+self.n-1]==0):
                self.storage[i] = j
                self.column[j] = self.slope1[i+j] = self.slope2[i-j+self.n-1] = 1
                if i==self.n-1:
                    self.output += 1
                else:
                    self.stepSolve(i+1)
                self.column[j] = self.slope1[i+j] = self.slope2[i-j+self.n-1] = 0
