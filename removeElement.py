#########################################################################
## LeetCode Number 27 Remove Element
## Problem description can be found here:
## https://leetcode.com/problems/remove-element/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.remove(nums[i])
        return len(nums)
