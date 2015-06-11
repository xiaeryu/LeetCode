#########################################################################
## LeetCode Number 137 Single Number II
## Problem description can be found here:
## https://leetcode.com/problems/single-number-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        storage = {}
        for item in nums:
            if item not in storage:
                storage[item] = 1
            else:
                storage[item] += 1
        
        for key in storage:
            if storage[key] < 3:
                return key
