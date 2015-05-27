#########################################################################
## LeetCode Number 53 Maximum Subarray
## Problem description can be found here:
## https://leetcode.com/problems/maximum-subarray/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        out=[]
        for i in range(0, len(nums)):
            if i==0:
                out.append(nums[i])
            else:
                out.append(max(nums[i],nums[i]+out[i-1]))
        return max(out)
