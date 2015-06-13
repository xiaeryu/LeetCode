#########################################################################
## LeetCode Number 13 Roman to Integer
## Problem description can be found here:
## https://leetcode.com/problems/roman-to-integer/
## Python script
#########################################################################

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        total = len(s)
        if total==0:
            return -1
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        p,q=0,1
        sum = 0
        while q<total:
            if roman[s[p]]<roman[s[q]]:
                sum+= ((-1)*roman[s[p]])
            else:
                sum += roman[s[p]]
            p,q=q,q+1
        sum+=roman[s[p]]
        return sum
