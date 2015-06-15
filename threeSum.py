#########################################################################
## LeetCode Number 15 3Sum
## Problem description can be found here:
## https://leetcode.com/problems/3sum/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def twoSum(self,nums,target):
        out = []
        for i in range(len(nums)-1):
            if target-nums[i] in nums[i+1:]:
                out.append([nums[i],target-nums[i]])
        return out

    def threeSum(self, nums):
        nums.sort()
        storage = []
        for i in range(len(nums)-2):
            tmp = self.twoSum(nums[i+1:],0-nums[i])
            if len(tmp) > 0:
                for item in tmp:
                    candidate = [nums[i]]+item
                    if candidate not in storage:
                        storage.append(candidate)

        return storage
