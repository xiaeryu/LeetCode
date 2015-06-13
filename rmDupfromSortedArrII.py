#########################################################################
## LeetCode Number 80 Remove Duplicates from Sorted Array II
## Problem description can be found here:
## https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        total = len(nums)
        if total < 2:
            return total
        flag = 0
        trace = nums[-1]
        for i in range(total-2,-1,-1):
            if nums[i]==trace:
                if flag==1:
                    del nums[i]
                else:
                    flag += 1
            else:
                trace = nums[i]
                flag = 0
        return len(nums)
