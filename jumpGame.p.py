#########################################################################
## LeetCode Number 55 Jump Game
## Problem description can be found here:
## https://leetcode.com/problems/jump-game/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        total = len(nums)
        if total < 2:
            return True
        
        if nums[0] == 0:
            return False

        stepsLeft = nums[0]
        for num in nums[1:-1]:
            stepsLeft = max(stepsLeft - 1, num)
            if stepsLeft==0:
                return False

        return True
