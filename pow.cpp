/*
#########################################################################
## LeetCode Number 50 Pow(x, n)
## Problem description can be found here:
## https://leetcode.com/problems/powx-n/
## C++ script
#########################################################################
*/

class Solution {
public:
    double myPow(double x, int n) {
        double minor = 1.0e-308;
        double out=1.0;
        if(abs(x) <= minor){
            return 0;
        }
        
        if(n==0){
            return 1;
        }
        if(n==1){
            return x;
        }
        
        x=(n>0)?x:(1/x);
        n=(n>0)?n:(-n);
        out = myPow(x,n/2);
        if(n%2==0){
            return out*out;
        }else{
            return out*out*x;
        }
    }    
};
