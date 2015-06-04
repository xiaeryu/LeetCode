#########################################################################
## LeetCode Number 28 Implement strStr()
## Problem description can be found here:
## https://leetcode.com/problems/implement-strstr/
## Python script
#########################################################################

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        ln = len(needle)
        lh = len(haystack)
        if ln==0:
            return 0
        if lh==0:
            return -1
        for i in range(lh-ln+1):
            if haystack[i] == needle[0]:
                flag = 1
                for j in range(1,ln):
                    if haystack[i+j] != needle[j]:
                        flag = 0
                        break
                if flag==1:
                    return i
        return -1
