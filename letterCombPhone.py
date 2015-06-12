#########################################################################
## LeetCode Number 17 Letter Combinations of a Phone Number
## Problem description can be found here:
## https://leetcode.com/problems/letter-combinations-of-a-phone-number/
## Python script
#########################################################################

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        ref = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}
        digits = digits.replace('1','')
        total = len(digits)
        if total == 0:
            return []
        if total ==1:
            return [item for item in ref[digits[0]]]
        
        new = ref[digits[-1]]
        result = self.letterCombinations(digits[:total-1])
        out = []
        for c in new:
            tmp = [old+c for old in result]
            out.extend(tmp)
        return out
