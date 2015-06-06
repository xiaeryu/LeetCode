#########################################################################
## LeetCode Number 33 Search in Rotated Sorted Array 
## Problem description can be found here:
## https://leetcode.com/problems/search-in-rotated-sorted-array/
## Python script
#########################################################################
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return -1
