#########################################################################
## LeetCode Number 34 Search for a Range
## Problem description can be found here:
## https://leetcode.com/problems/climbing-stairs/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        total = len(nums)
        if total == 0:
            return [-1,-1]
        if total == 1:
            if target == nums[0]:
                return [0,0]
            else:
                return [-1,-1]
        
        mid = total/2 - 1
        t = Solution()
        if nums[mid]<target:
            tmp = t.searchRange(nums[mid+1:],target)
            if tmp == [-1,-1]:
                return tmp
            else:
                return [tmp[0]+mid+1,tmp[1]+mid+1]
        elif nums[mid]>target:
            tmp = t.searchRange(nums[:mid],target)
            return tmp
        else:
            start = mid
            end = mid
            flag = 0
            for i in range(1,mid+1):
                if nums[mid-i]!=target:
                    start = mid-i+1
                    flag = 1
                    break
            if flag==0:
                start = 0
            flag = 0
            for j in range(1,total-mid):
                if nums[mid+j]!=target:
                    end = mid+j-1
                    flag =1
                    break
            if flag==0:
                end = total-1
            return [start,end]
