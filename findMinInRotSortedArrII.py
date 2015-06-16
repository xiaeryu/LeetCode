#########################################################################
## LeetCode Number 154 Find Minimum in Rotated Sorted Array II 
## Problem description can be found here:
## https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        return sorted(nums)[0]
