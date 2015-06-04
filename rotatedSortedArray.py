# -*- coding: utf-8 -*-

#################################################################
## LeetCode – Find Minimum in Rotated Sorted Array
##
## Suppose a sorted array is rotated at some pivot unknown to you
## beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
## Find the minimum element.You may assume no duplicate exists in
## the array.
#################################################################
## A divide-and-conquer approach
#################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        return sorted(nums)[0]
