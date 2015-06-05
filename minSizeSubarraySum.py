#########################################################################
## LeetCode Number 209 Minimum Size Subarray Sum
## Problem description can be found here:
## https://leetcode.com/problems/minimum-size-subarray-sum/
## Python script
#########################################################################

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        total = len(nums)
        if total==0:
            return 0
        if nums[0] >= s:
            return 1
        if total==1:
            return 0
                
        start = 0
        end = 1
        tmp = nums[0]
        minLen = total+1
        while end<total:
            tmp += nums[end]
            while tmp >= s:
                here = end-start+1
                if here < minLen:
                    minLen = here
                tmp -= nums[start]
                start += 1
            end += 1
        
        if minLen > total:
                return 0
        else:
                return minLen
