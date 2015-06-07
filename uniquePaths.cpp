/*
#########################################################################
## LeetCode Number 62 Unique Paths
## Problem description can be found here:
## https://leetcode.com/problems/unique-paths/
## C++
#########################################################################
*/

class Solution {
public:
    int uniquePaths(int m, int n) {
        long out = 1;
        int small = (m<n)?m:n;
        int big = (m>n)?m:n;
        for(int j=big;j<=(big+small-2);j++){
            out *= j;
        }
        for(int i=2;i<=small-1;i++){
            out /= i;
        }
        return out;
    }
};
