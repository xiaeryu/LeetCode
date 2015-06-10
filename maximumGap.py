#########################################################################
## LeetCode Number 164 Maximum Gap
## Problem description can be found here:
## https://leetcode.com/problems/maximum-gap/
## Python script
#########################################################################

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        total = len(nums)
        if total < 2:
            return 0
        A = min(nums)
        B = max(nums)
        bucketRange = max(1, int((B - A - 1) / (total - 1)) + 1)
        bucketLen = (B - A) / bucketRange + 1
        buckets = [None] * bucketLen
        for K in nums:
            loc = (K - A) / bucketRange
            bucket = buckets[loc]
            if bucket is None:
                bucket = {'min' : K, 'max' : K}
                buckets[loc] = bucket
            else:
                bucket['min'] = min(bucket['min'], K)
                bucket['max'] = max(bucket['max'], K)
        maxGap = 0
        for x in range(bucketLen):
            if buckets[x] is None:
                continue
            y = x + 1
            while y < bucketLen and buckets[y] is None:
                y += 1
            if y < bucketLen:
                maxGap = max(maxGap, buckets[y]['min'] - buckets[x]['max'])
            x = y
        return maxGap
