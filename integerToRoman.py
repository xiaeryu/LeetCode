#########################################################################
## LeetCode Number 12 Integer to Roman
## Problem description can be found here:
## https://leetcode.com/problems/add-binary/
## Python script
#########################################################################

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        result = num//1000 *'M' + num%1000//100*'C' + num%1000%100//10*'X' + num%1000%100%10*'I'

        result = result.replace('IIIIIIIII', 'IX')
        result = result.replace('IIIII','V')
        result = result.replace('IIII' , 'IV')
        result = result.replace('XXXXXXXXX', 'XC')
        result = result.replace('XXXXX' , 'L')
        result = result.replace('XXXX' , 'XL')
        result = result.replace('CCCCCCCCC', 'CM')
        result = result.replace('CCCCC', 'D')
        result = result.replace('CCCC', 'CD')
        
        return result
