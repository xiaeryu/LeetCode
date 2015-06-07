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
        
        storage = [0 for i in range(total)]
        if nums[0] != 0:
            storage[0] = 1
        ind = 0
        while ind < total:
            if storage[ind] == 1:
                for m in range(1,min(nums[ind]+1,total-ind)):
                    storage[ind+m] = 1
            ind += 1

        if storage[total-1]==1:
            return True
        else:
            return False
