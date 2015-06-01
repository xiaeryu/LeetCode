#########################################################################
## LeetCode Number 8 String to Integer (atoi)
## Problem description can be found here:
## https://leetcode.com/problems/string-to-integer-atoi/
## Python script
#########################################################################

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        mark = 0
        str = str.lstrip(' ')
        if len(str) > 1:
            if str[0] == '-':
                mark = 1
                str = str[1:]
            elif str[0] == '+':
                str = str[1:]
        str = str.lstrip('0')
        flag = 0
        result = 0
        for i in range(len(str)-1,-1,-1):
            if ord(str[i])>=48 and ord(str[i])<=57:
                result += 10**flag * (ord(str[i])-48)
                flag += 1
            else:
                result = 0
                flag = 0
        if mark==1:
            if result >= 2147483648:
                return -2147483648
            else:
                return -1 * result
        else:
            if result > 2147483647:
                return 2147483647
            else:
                return result
