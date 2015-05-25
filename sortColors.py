class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        storage = [0,0,0]
        for num in nums:
            storage[num] += 1
        for i in range(1,storage[0]+1):
            nums[i-1] = 0
        for i in range(storage[0]+1,storage[0]+storage[1]+1):
            nums[i-1] = 1
        for i in range(storage[0]+storage[1]+1,len(nums)+1):
            nums[i-1] = 2
