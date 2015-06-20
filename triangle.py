#########################################################################
## LeetCode Number 120 Triangle 
## Problem description can be found here:
## https://leetcode.com/problems/triangle/
## Python script
#########################################################################

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        total = len(triangle)
        storage = [0 for i in range(total+1)]
        for i in range(total-1,-1,-1):
            tmp = triangle[i]
            for j in range(len(tmp)):
                storage[j] = tmp[j] + min(storage[j], storage[j + 1])

        return storage[0]
