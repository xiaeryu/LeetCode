#########################################################################
## LeetCode Number 191 Number of 1 Bits
## Problem description can be found here:
## https://leetcode.com/problems/number-of-1-bits/
## Python script
#########################################################################

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        sum = 0
        out = str("{0:b}".format(n))
        for i in out:
            sum += int(i)
        return sum
