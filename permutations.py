#########################################################################
## LeetCode Number 46 Permutations 
## Problem description can be found here:
## https://leetcode.com/problems/permutations/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        total = len(nums)
        self.nums = nums
        self.n = total
        self.storage = [-1] * total
        self.output = []
        self.rec = [0] * total
        self.generate(0)
        return self.output

    def generate(self,i):
        for j in range(self.n):
            if (self.rec[j] == 0):
                self.storage[i] = j
                self.rec[j] = 1
                if i == self.n - 1:
                    self.output.append([self.nums[item] for item in self.storage])
                else:
                    self.generate(i+1)
                self.rec[j] = 0
