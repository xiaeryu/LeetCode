/*
#########################################################################
## LeetCode Number 168 Excel Sheet Column Title
## Problem description can be found here:
## https://leetcode.com/problems/excel-sheet-column-title/
## C++ script
#########################################################################
*/

class Solution {
public:
    string convertToTitle(int n) {
        string out="";
        while(n!=0){
            char bit=('A'+((n-1)%26));
            out = bit + out;
            n=(n-1)/26;
        }
        return out;
    }
};
