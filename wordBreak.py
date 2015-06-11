#########################################################################
## LeetCode Number 139 Word Break
## Problem description can be found here:
## https://leetcode.com/problems/word-break/
## Python script
#########################################################################

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        total = len(s)
        if total == 0:
            return True
        storage = [False for m in range(total)]
        if s[0] in wordDict:
            storage[0] = True
        
        for i in range(total):
            if s[:i+1] in wordDict:
                storage[i] = True
            else:
                for j in range(i-1,-1,-1):
                    if storage[j]:
                        if s[j+1:i+1] in wordDict:
                            storage[i] = True
                            break
            
        return storage[total-1]
