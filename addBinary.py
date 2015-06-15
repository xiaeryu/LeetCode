#########################################################################
## LeetCode Number 67 Add Binary 
## Problem description can be found here:
## https://leetcode.com/problems/add-binary/
## Python script
#########################################################################

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def str2bin(self,s):
        total = len(s)
        out = 0
        for i in range(total-1,-1,-1):
            out += int(s[i])*pow(2,total-1-i)
        return out

    def addBinary(self, a, b):
        val = self.str2bin(a) + self.str2bin(b)
        return "{0:b}".format(val)
