#########################################################################
## LeetCode Number 35 Search Insert Position
## Problem description can be found here:
## https://leetcode.com/problems/search-insert-position/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        for i in range(0,len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)
