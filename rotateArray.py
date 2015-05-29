#########################################################################
## LeetCode Number 189 Rotate Array
## Problem description can be found here:
## https://leetcode.com/problems/rotate-array/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        point = len(nums) - k
        nums[:] = nums[point:] + nums[:point]
