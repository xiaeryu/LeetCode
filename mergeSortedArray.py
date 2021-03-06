#########################################################################
## LeetCode Number 88 Merge Sorted Array
## Problem description can be found here:
## https://leetcode.com/problems/merge-sorted-array/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()
