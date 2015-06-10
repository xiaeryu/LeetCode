#########################################################################
## LeetCode Number 70 Maximum Product Subarray
## Problem description can be found here:
## https://leetcode.com/problems/maximum-product-subarray/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        total = len(nums)
        if total == 0:
            return 0
        if total == 1:
            return nums[0]
        if 0 not in nums:
            prod = reduce(lambda x,y :x*y,nums)
            if prod > 0:
                return prod
            else:
                left = prod
                right = prod
                li = 0
                ri = total-1
                while nums[li] > 0:
                    left /= nums[li]
                    li += 1
                left /= nums[li]

                while nums[ri] > 0:
                    right /= nums[ri]
                    ri -= 1
                right /= nums[ri]
                return max(left,right)
        else:
            return max(self.maxProduct(nums[:nums.index(0)]),self.maxProduct(nums[nums.index(0)+1:]),0)
