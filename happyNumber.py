#########################################################################
## LeetCode Number 202 Happy Number
## Problem description can be found here:
## https://leetcode.com/problems/happy-number/
## Python script
#########################################################################
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        if n ==1:
            return True
        
        s = Solution()
        storage = {}
        while n != 1:
            if n in storage:
                return False
            else:
                storage[n] = 1
                sum = 0
                for i in str(n):
                    sum += int(i)**2
                n = sum
        return True
