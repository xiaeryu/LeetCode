#########################################################################
## LeetCode Number 122 Best Time to Buy and Sell Stock II 
## Problem description can be found here:
## https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        total = len(prices)
        if total <2:
            return 0
        curr = 0
        mm = 0
        for i in range(1,total):
            diff = prices[i] - prices[i-1]
            if diff >= 0:
                curr += diff
            else:
                mm += curr
                curr = 0
        return mm+curr
