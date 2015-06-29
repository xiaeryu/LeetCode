#########################################################################
## LeetCode Number 228 Summary Ranges  
## Problem description can be found here:
## https://leetcode.com/problems/summary-ranges/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        total = len(nums)
        if total == 0:
            return []
        front = nums[0] # The front of the range
        back = nums[0] # The back of the range
        output = [] # Store the output results
        
        for i in range(1,total):
            if nums[i] == front + 1:
                front = nums[i]
            else:
                if back != front:
                    output.append(str(back) + "->" + str(front))
                else:
                    output.append(str(back))
                front = back = nums[i]
        if back != front:
            output.append(str(back) + "->" + str(front))
        else:
            output.append(str(back))
        return output
