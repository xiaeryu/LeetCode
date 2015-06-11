#########################################################################
## LeetCode Number 140 Word Break II 
## Problem description can be found here:
## https://leetcode.com/problems/word-break-ii/
## Python script
#########################################################################

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        self.dict = dict
        self.cache = {}
        return self.break_helper(s)

    def break_helper(self, s):
        combs = []
        if s in self.cache:
            return self.cache[s]
        if len(s) == 0:
            return []

        for i in range(len(s)):
            if s[:i+1] in self.dict:
                if i == len(s) - 1:
                    combs.append(s[:i+1])
                else:
                    sub_combs = self.break_helper(s[i+1:])
                    for sub_comb in sub_combs:
                        combs.append(s[:i+1] + ' ' + sub_comb)

        self.cache[s] = combs
        return combs
