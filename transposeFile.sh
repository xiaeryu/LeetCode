#########################################################################
## LeetCode Number 194 Transpose File
## Problem description can be found here:
## https://leetcode.com/problems/transpose-file/
#########################################################################

total=`head -1 file.txt | awk '{print NF}'`; for((i=1;i<=$total;i++)); do awk -v var=${i} '{printf $var " "}' file.txt | sed 's/ $//'; echo; done
