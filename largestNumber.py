#########################################################################
## LeetCode Number 179 Largest Number 
## Problem description can be found here:
## https://leetcode.com/problems/largest-number/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def compare(self,str1,str2):
        if (str1 + str2) > (str2 + str1):
            return -1
        else:
            return 1

    def largestNumber(self, nums):
        num = sorted([str(i) for i in nums], cmp = self.compare)
        ans = ''.join(num).lstrip('0')
        return ans or '0'
