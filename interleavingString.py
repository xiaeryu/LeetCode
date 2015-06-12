#########################################################################
## LeetCode Number 97 Interleaving String
## Problem description can be found here:
## https://leetcode.com/problems/interleaving-string/
## Python script
#########################################################################

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        total = len(s3)
        if total != len(s1) + len(s2):
            return False

        dp = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        for i in range(0, len(s1)+1):
            for j in range(0, len(s2)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:                        #"aa", "ab", "abaa" length of s1 is 0
                    dp[i][j] = s2[:j] == s3[:j]
                elif j == 0:                        #length of s2 is 0
                    dp[i][j] = s1[:i] == s3[:i]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]
