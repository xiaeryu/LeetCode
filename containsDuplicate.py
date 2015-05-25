#########################################################################
## LeetCode Number 217 Contains Duplicate
## Problem description can be found here:
## https://leetcode.com/problems/contains-duplicate/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        previous = {}
        for num in nums:
            if num in previous:
                return True
            else:
                previous[num] = 1
        return False
