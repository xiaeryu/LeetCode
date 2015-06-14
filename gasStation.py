#########################################################################
## LeetCode Number 134 Gas Station 
## Problem description can be found here:
## https://leetcode.com/problems/gas-station/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        accumulate=0
        minaccu=0
        start=0

        for i in range(len(gas)):
            accumulate+=gas[i]-cost[i]
            if accumulate<minaccu:
                minaccu=accumulate
                start=i+1

        if accumulate<0:
            return -1

        return start
