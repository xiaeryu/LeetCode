#########################################################################
## LeetCode Number 96 Unique Binary Search Trees
## Problem description can be found here:
## https://leetcode.com/problems/unique-binary-search-trees/
## Python script
#########################################################################

class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        storage = [0 for i in range(n+1)]
        storage[0] = 1
        storage[1] = 1
        
        for i in range(2,n+1):
            for j in range(i):
                storage[i] += storage[j] * storage[i-j-1]
        
        return storage[n]
