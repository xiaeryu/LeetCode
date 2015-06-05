/*
#########################################################################
## LeetCode Number 136 Single Number 
## Problem description can be found here:
## https://leetcode.com/problems/single-number/
## C++ script
#########################################################################
*/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result=0;
        for(int i = 0;i<nums.size();i++){
            result = result^nums[i];
        }
        return result;
    }
};
