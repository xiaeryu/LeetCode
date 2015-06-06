#########################################################################
## LeetCode Number 81 Search in Rotated Sorted Array II 
## Problem description can be found here:
## https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        if target in nums:
            return True
        else:
            return False
