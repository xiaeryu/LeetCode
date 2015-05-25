class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        previous = {}
        for num in nums:
            if num in previous:
                return True
            else:
                previous[num] = 1
        return False
