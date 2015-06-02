#########################################################################
## LeetCode Number 58 Length of Last Word
## Problem description can be found here:
## https://leetcode.com/problems/length-of-last-word/
## Python script
#########################################################################

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s = s.strip(' ')
        s = s.lstrip(' ')
        tmp = s.split(' ')
        if len(tmp) == 0:
            return 0
        else:
            return len(tmp[len(tmp)-1])
