#########################################################################
## LeetCode Number 5 Longest Palindromic Substring
## Problem description can be found here:
## https://leetcode.com/problems/longest-palindromic-substring/
## Python script
#########################################################################

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        total = len(s)
        if total <= 1:
            return s
        rev = s[::-1]
        storage = [[0 for i in range(total)] for k in range(total)]
        maxVal = -1
        maxPos = -1
        for i in range(total):
            for j in range(total):
                if s[i]==rev[j]:
                    if i*j ==0:
                        storage[i][j] = 1
                    else:
                        storage[i][j] = storage[i-1][j-1]+1
                if storage[i][j]>maxVal:
                    maxVal = storage[i][j]
                    maxPos = j
        
        return rev[maxPos+1-maxVal:maxPos+1]
