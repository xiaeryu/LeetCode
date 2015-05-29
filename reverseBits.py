#########################################################################
## LeetCode Number 190  Reverse Bits
## Problem description can be found here:
## https://leetcode.com/problems/reverse-bits/
## Python script
#########################################################################

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin = "{0:b}".format(n)
        bin = bin[::-1]
        bin += '0'*(32-len(bin))
        return int(bin, 2)
