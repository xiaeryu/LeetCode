#########################################################################
## LeetCode Number 77 Combinations
## Problem description can be found here:
## https://leetcode.com/problems/combinations/
## Python script
#########################################################################

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if k == 0:
            return[[]]
        if k == n:
            return[[i for i in range(1,n+1)]]
        
        bk1 = self.combine(n-1,k-1)
        for i in range(len(bk1)):
            bk1[i].append(n)
        bk1 += self.combine(n-1,k)
        return bk1
