#########################################################################
## LeetCode Number 91 Decode Ways
## Problem description can be found here:
## https://leetcode.com/problems/decode-ways/
## Python script
#########################################################################

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        this = len(s)
        if this ==0:
            return 0
        if s[0] == '0':
            return 0
        if this ==1:
            return 1

        storage = [0 for i in range(this)]
        storage[0] = 1

        if int(s[0])>0 and int(s[1])>0 and int(s[:2]) <=26:
            storage[1] = 2
        elif int(s[0]) >0 and int(s[1])>0:
            storage[1] = 1
        elif int(s[:2]) in [10,20]:
            storage[1] = 1
        else:
            storage[1] = 0
        
        if len(s) == 2:
            return storage[1]

        for total in range(2,this):
            if int(s[total]) == 0:
                if int(s[total-1]) > 0 and int(s[total-1]) < 3:
                    storage[total] = storage[total-2]
                else:
                    storage[total] = 0
            elif int(s[total-1]) != 0 and int(s[total-1:total+1]) <= 26:
                storage[total] = storage[total-1] + storage[total-2]
            else:
                storage[total] = storage[total-1]
        return storage[this-1]
