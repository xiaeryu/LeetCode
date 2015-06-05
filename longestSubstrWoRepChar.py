#########################################################################
## LeetCode Number 3 Longest Substring Without Repeating Characters
## Problem description can be found here:
## https://leetcode.com/problems/longest-substring-without-repeating-characters/
## Python script
#########################################################################

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        ref = {}
        start = 0
        tmpMax = 1
        for i in range(len(s)):
            if s[i] in ref and start<= ref[s[i]]:
                start = ref[s[i]]+1
            else:
                tmpMax = max(tmpMax,i-start+1)
            ref[s[i]]=i
        return tmpMax
