#########################################################################
## LeetCode Number 20 Valid Parentheses
## Problem description can be found here:
## https://leetcode.com/problems/valid-parentheses/
## Python script
#########################################################################

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        array = [s[0]]
        for i in range(1,len(s)):
            if s[i] in ['(','{','[']:
                array.append(s[i])
            elif s[i] == ')':
                if len(array)>0 and array[len(array)-1] == '(':
                    array.pop()
                else:
                    return False
            elif s[i] == '}':
                if len(array)>0 and array[len(array)-1] == '{':
                    array.pop()
                else:
                    return False
            elif s[i] == ']':
                if len(array)>0 and array[len(array)-1] == '[':
                    array.pop()
                else:
                    return False
        if len(array)==0:
            return True
        else:
            return False
