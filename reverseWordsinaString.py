#########################################################################
## LeetCode Number 151 Reverse Words in a String
## Problem description can be found here:
## https://leetcode.com/problems/reverse-words-in-a-string/
## Python script
#########################################################################

import re

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip(' ')
        s = s.lstrip(' ')
        tmp = re.split('\s+',s)
        outs = tmp[len(tmp)-1]
        for i in range(len(tmp)-2,-1,-1):
            outs = outs + " " + tmp[i]
        return outs
