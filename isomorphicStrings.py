#########################################################################
## LeetCode Number 205 Isomorphic Strings 
## Problem description can be found here:
## https://leetcode.com/problems/isomorphic-strings/
## Python script
#########################################################################

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        if s == t:
            return True
        dic = {}
        for i in range(len(s)):
            if (s[i] in dic) and (t[i]==dic[s[i]]):
                pass 
            elif (s[i] in dic):
                return False
            elif t[i] in dic.values():
                return False
            else:
                dic[s[i]]=t[i]
        return True
