#########################################################################
## LeetCode Number 162 Find Peak Element
## Problem description can be found here:
## https://leetcode.com/problems/find-peak-element/
## Python script
#########################################################################

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        total = len(nums)
        if total <= 1:
            return 0
        if nums[0]>nums[1]:
                return 0
        elif nums[total-1]>nums[total-2]:
            return total-1
        elif total == 3:
            if nums[0]<nums[1] and nums[1]>nums[2]:
                return 1
            else:
                return -1
        mid = total/2-1
        t=Solution()
        if nums[mid]<nums[mid-1]:
            result = t.findPeakElement(nums[:mid])
        elif nums[mid]<nums[mid+1]:
            result = mid +1+ t.findPeakElement(nums[mid+1:])
        else:
            result = mid
            
        return result
