#########################################################################
## LeetCode Number 121 Best Time to Buy and Sell Stock
## Problem description can be found here:
## https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        total = len(prices)
        if total < 2:
            return 0
        if total == 2:
            return [0,prices[1]-prices[0]][prices[1]>prices[0]]

        middle = total/2
        return max(self.maxProfit(prices[:middle]),self.maxProfit(prices[middle:]),max(prices[middle:])-min(prices[:middle]))
