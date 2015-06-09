/*
#########################################################################
## LeetCode Number 69 Sqrt(x) 
## Problem description can be found here:
## https://leetcode.com/problems/sqrtx/
## C++ script
#########################################################################
*/

class Solution {
public:
    int mySqrt(int x) {
        long start=0;
        long end=x;
        while(start <= end){
            long middle = (start+end)/2;
            long product = middle*middle;
            if(product > x){
                end = middle-1;
            }else if(product < x){
                start = middle +1;
            }else{
                return middle;
            }
        }
        return end;
    }
};
