#########################################################################
## LeetCode Number 7 Reverse Integer
## Problem description can be found here:
## https://leetcode.com/problems/reverse-integer/
## Python script
#########################################################################

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        flag = False
        if x<0:
            flag=True
            x = -x
        out = str(x)[::-1]
        out.lstrip("0")
        out = int(out)
        if flag:
            out = -out
        if out > 2147483647 or out < -2147483646:
            return 0
        return out
