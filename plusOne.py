#########################################################################
## LeetCode Number 66 Plus One
## Problem description can be found here:
## https://leetcode.com/problems/plus-one/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        length = len(digits)
        t = Solution()
        if length==0:
            return []
        if length==1 and digits[0] == 9:
            digits = [1,0]
            return digits
        if digits[length-1] < 9:
            digits[length-1] += 1
            return digits
        else:
            digits[length-1] = 0
            tmp = t.plusOne(digits[:length-1])
            tmp.append(0)
            return tmp
