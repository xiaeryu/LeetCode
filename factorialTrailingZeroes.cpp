/*
#########################################################################
## LeetCode Number 172 Factorial Trailing Zeroes 
## Problem description can be found here:
## https://leetcode.com/problems/factorial-trailing-zeroes/
## C++ script
#########################################################################
*/

class Solution {
public:
    int trailingZeroes(int n) {
        int sum = 0;
        for(int i=1;pow(5,i)<=n;i++){
            sum += (n/pow(5,i));
        }
        return sum;
    }
};
