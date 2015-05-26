#########################################################################
## LeetCode Number 169 Majority Element
## Problem description can be found here:
## https://leetcode.com/problems/majority-element/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        storage = {}
        for i in nums:
           if i in storage:
               storage[i] += 1
           else:
               storage[i] = 1
        
        for i in storage:
            if storage[i] > int(len(nums)/2):
                return i
