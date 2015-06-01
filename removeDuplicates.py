
#########################################################################
## LeetCode Number 26 Remove Duplicates from Sorted Array
## Problem description can be found here:
## https://leetcode.com/problems/remove-duplicates-from-sorted-array/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        trace = nums[0]
        count = 1
        for i in nums:
            if i!= trace:
                count += 1
                nums[count-1]=i
                trace = i
        return count
