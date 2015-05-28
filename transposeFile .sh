#########################################################################
## LeetCode Number 194 Transpose File
## Problem description can be found here:
## https://leetcode.com/problems/transpose-file/
#########################################################################

## This script exceeds the memory limit when the file is very large, thus works only for smaller files.

# Read from the file file.txt and print its transposed content to stdout.
total=`head -1 file.txt | awk '{print NF}'`; for i in `seq 1 $total`; do awk -v var=${i} '{printf $var " "}' file.txt | sed 's/ $//'; echo; done
