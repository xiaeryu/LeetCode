/*
#########################################################################
## LeetCode Number 171 Excel Sheet Column Number
## Problem description can be found here:
## https://leetcode.com/problems/climbing-stairs/
## C++ script
#########################################################################
*/

class Solution {
public:
    int titleToNumber(string s) {
        int digit = s.length();
        if(digit==0){return 0;}
        char array[digit];
        strcpy(array,s.c_str());
        int out = 0;
        for(int i=0;i<digit;i++){
            out += (array[i]-'A'+1) * pow(26,digit-i-1);
        }
        return out;
    }
};
