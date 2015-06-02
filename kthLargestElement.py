#########################################################################
## LeetCode Number 215 Kth Largest Element in an Array
## Problem description can be found here:
## https://leetcode.com/problems/kth-largest-element-in-an-array/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        return sorted(nums,reverse=True)[k-1]
