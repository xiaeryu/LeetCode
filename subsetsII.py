#########################################################################
## LeetCode Number 90 Subsets II 
## Problem description can be found here:
## https://leetcode.com/problems/subsets-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        if len(nums) == 0:
            return [[]]
        
        nums.sort()
        out = [[],[nums[0]]]

        for i in range(1,len(nums)):
            tmp = []
            for arr in out:
                here = arr[:]
                here.append(nums[i])
                tmp.append(here[:])
            for item in tmp:
                if item not in out:
                    out.append(item[:])
        
        return out
