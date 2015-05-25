######################################################################
## LeetCode Number 193 Valid Phone Numbers 
## Problem description can be found here:
## https://leetcode.com/problems/valid-phone-numbers/
######################################################################

grep -v '^ \+' file.txt | grep -v ' \+$' | grep '^[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}$\|^([0-9]\{3\})\ [0-9]\{3\}-[0-9]\{4\}$'
