#########################################################################
## LeetCode Number 219 Contains Duplicate II 
## Problem description can be found here:
## https://leetcode.com/problems/contains-duplicate-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        storage = {}
        for i in range(0,len(nums)):
            if nums[i] in storage:
                if i - storage[nums[i]] <= k:
                    return True
                else:
                    storage[nums[i]] = i
            else:
                storage[nums[i]] = i
        return False
