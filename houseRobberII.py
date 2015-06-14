#########################################################################
## LeetCode Number 213 House Robber II
## Problem description can be found here:
## https://leetcode.com/problems/house-robber-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def robL(self, nums):
        total = len(nums)
        if total == 0:
            return 0
        elif total == 1:
            return nums[0]
        elif total == 2:
            return max(nums[0], nums[1])
        
        storage = [0 for i in range(total)]
        storage[0] = nums[0]
        storage[1] = max(nums[0], nums[1])

        for i in range(2,total):
            storage[i] = max(storage[i-1], nums[i] + storage[i-2])
        return storage[-1]
    
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.robL(nums[1:]),self.robL(nums[:len(nums)-1]))
