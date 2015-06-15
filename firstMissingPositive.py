#########################################################################
## LeetCode Number 41 First Missing Positive
## Problem description can be found here:
## https://leetcode.com/problems/first-missing-positive/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        total = len(nums)
        for i in range(total):
            while nums[i] >0 and nums[i] <= total and (nums[nums[i]-1] != nums[i]):
                tmp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[tmp-1] = tmp

        for j in range(total):
            if nums[j] != j+1:
                return j+1

        return total+1
