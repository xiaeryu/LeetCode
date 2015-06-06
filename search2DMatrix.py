#########################################################################
## LeetCode Number 74 Search a 2D Matrix
## Problem description can be found here:
## https://leetcode.com/problems/climbing-stairs/
## Python script
#########################################################################

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchBin(self,arr,target):
        fl = len(arr)
        if fl == 0:
            return False
        if fl == 1:
            if arr[0]==target:
                return True
            else:
                return False
                
        half = fl/2-1
        if arr[half]==target:
            return True
        elif arr[half] >= target:
            return self.searchBin(arr[:half],target)
        else:
            return self.searchBin(arr[half+1:],target)
        
    def searchMatrix(self, matrix, target):
        total = len(matrix)
        t=Solution()
        if total == 0:
            return False
        if total == 1:
            if matrix[0][0]>target or matrix[0][len(matrix[0])-1]<target:
                return False
            else:
                return t.searchBin(matrix[0],target)
        
        mid = total/2-1
        if matrix[mid][0]<=target and matrix[mid][len(matrix[mid])-1]>=target:
            return t.searchBin(matrix[mid],target)
        elif matrix[mid][len(matrix[0])-1]<target:
            return t.searchMatrix(matrix[mid+1:],target)
        else:
            return t.searchMatrix(matrix[:mid],target)
            
        return False
