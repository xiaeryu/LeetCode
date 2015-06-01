#########################################################################
## LeetCode Number 165 Compare Version Numbers
## Problem description can be found here:
## https://leetcode.com/problems/compare-version-numbers/
## Python script
#########################################################################

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}

    def compareVersion(self, version1, version2):
        str1 = version1.split('.')
        str2 = version2.split('.')
        
        i = 0
        while(len(str1)>i or len(str2)>i):
            if(len(str1)<=i):
                str1.append(0)
            if(len(str2)<=i):
                str2.append(0)
            digit1 = int(str1[i])
            digit2 = int(str2[i])
            if(digit1 > digit2):
                return 1
            elif(digit1 < digit2):
                return -1
            else:
                i += 1
        return 0
