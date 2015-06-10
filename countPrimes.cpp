/*
#########################################################################
## LeetCode Number 204 Count Primes
## Problem description can be found here:
## https://leetcode.com/problems/count-primes/
## C++ script
#########################################################################
*/

#include<math.h>

class Solution {
public:
    int countPrimes(int n) {
        if(n<=2){
            return 0;
        }
        vector<bool> storage(n,true);
        storage[0] = false;
        storage[1] = false;

        for(int i=2;i<=sqrt(n);i++){
            if(storage[i]){
                for(int j=pow(i,2);j<n;j+=i){
                        storage[j] = 0;
                }
            }
        }
        
        int total;
        for(int k =2;k<n;k++){
            total += storage[k];
        }
        return total;
    }
};
