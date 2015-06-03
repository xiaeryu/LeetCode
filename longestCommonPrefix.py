#########################################################################
## LeetCode Number 14 Longest Common Prefix
## Problem description can be found here:
## https://leetcode.com/problems/longest-common-prefix/
## Python script
#########################################################################

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        count = 0
        out = ""
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        minlen = len(strs[0])
        for str in strs:
            if len(str) < minlen:
                minlen = len(str)
        
        for i in range(minlen):
            signal = 1
            for j in range(1,len(strs)):
                if strs[j][i] != strs[0][i]:
                    signal = 0
                    break
            if signal == 0:
                return out
            else:
                out += strs[0][i]
                count += 1
        return out
