#########################################################################
## LeetCode Number 119 Pascal's Triangle II
## Problem description can be found here:
## https://leetcode.com/problems/pascals-triangle-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def generateNext(self,inarray):
        outarray = [1 for i in range(len(inarray)+1)]
        for j in range(2,len(outarray)):
            outarray[j-1] = inarray[j-2]+inarray[j-1]
        return outarray
        
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        
        initial = [1,2,1]
        out = [1,2,1]
        t = Solution()
        for i in range(2,rowIndex):
            out = t.generateNext(initial)
            initial = out
        return out
