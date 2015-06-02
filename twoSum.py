#########################################################################
## LeetCode Number 1 Two Sum
## Problem description can be found here:
## https://leetcode.com/problems/two-sum/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        storage = {}
        outlist = [0,0]
        for i in range(len(nums)):
            if nums[i] in storage:
                storage[nums[i]] += 1
            else:
                storage[nums[i]] = 1
                
        for i in range(len(nums)-1,-1,-1):
            if (target-nums[i])==nums[i]:
                if storage[nums[i]]>=2:
                    outlist[1] = i+1
                    outlist[0] = nums.index(nums[i])+1
                    break
            else:
                if (target-nums[i]) in storage:
                    outlist[1] = i+1
                    outlist[0] = nums.index(target - nums[i])+1
                    break
        
        return outlist
