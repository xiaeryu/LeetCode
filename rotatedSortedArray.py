# -*- coding: utf-8 -*-

#################################################################
## LeetCode – Find Minimum in Rotated Sorted Array
##
## Suppose a sorted array is rotated at some pivot unknown to you
## beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
## Find the minimum element.You may assume no duplicate exists in
## the array.
#################################################################
## A divide-and-conquer approach
#################################################################

def compareHT(inArray):
    lenArray = len(inArray)
    if lenArray <= 3:
        return min(inArray)
    else:
        half = int((lenArray-1)/2)
        if inArray[0] > inArray[half]:
            return compareHT(inArray[:half+1])
        else:
            return compareHT(inArray[half+1:])

realArray = range(28,1000000)
testArray = realArray[10000:] + realArray[:10000]
print compareHT(testArray)
