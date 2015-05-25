################################################################################
## LeetCode Number 192. Word Frequency
## Write a bash script to calculate the frequency of each word in a text file words.txt
## The problem is elaborated here: https://leetcode.com/problems/word-frequency/
################################################################################

sed 's/[[:space:]]\+/\n/g' words.txt | sort | uniq -c | sort -nrk1 | awk '{print $2 " " $1}'
