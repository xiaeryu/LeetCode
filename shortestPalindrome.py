#########################################################################
## LeetCode Number 214 Shortest Palindrome
## Problem description can be found here:
## https://leetcode.com/problems/shortest-palindrome/
## Python script
#########################################################################

class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        total = len(s)
        if total <= 1:
            return s
        rev = s[::-1]
        string = s + rev
        storage = [0 for i in range(total*2)]
        for i in range(1, 2*total):
            j = storage[i - 1]
            while j > 0 and string[i] != string[j]:
                j = storage[j - 1]
            storage[i] = j + (string[i] == string[j])
        return rev[: total-storage[-1]] + s
