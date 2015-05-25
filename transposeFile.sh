#########################################################################
## LeetCode Number 194 Transpose File
## Problem description can be found here:
## https://leetcode.com/problems/transpose-file/
#########################################################################

awk '{printf $1 " "}' file.txt | sed 's/ $/\n/'; awk '{printf $2 " "}' file.txt | sed 's/ $/\n/'
