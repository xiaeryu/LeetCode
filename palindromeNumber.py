#########################################################################
## LeetCode Number 9 Palindrome Number 
## Problem description can be found here:
## https://leetcode.com/problems/palindrome-number/
## Python script
#########################################################################

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
            
        digit = 1
        tmp = x
        while tmp/10 >= 1:
            digit += 1
            tmp = tmp/10
        
        for i in range(1,int(digit/2)+1):
            if x%10 != x/10**(digit+1-2*i):
                return False
            x = x%10**(digit+1-2*i)
            x = x/10
        
        return True
