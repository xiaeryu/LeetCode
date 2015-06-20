#########################################################################
## LeetCode Number 89 Gray Code  
## Problem description can be found here:
## https://leetcode.com/problems/gray-code/
## Python script
#########################################################################

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        storage = [0]
        for i in range(n):
            storage += [x + pow(2, i) for x in reversed(storage)]
        return storage
