/*
#########################################################################
## LeetCode Number 125 Valid Palindrome 
## Problem description can be found here:
## https://leetcode.com/problems/valid-palindrome/
## C++ script
#########################################################################
*/

class Solution {
public:
    bool isPalindrome(string s) {
        int len=s.length();
        if (len == 0){return true;}
        char storage[len];
        int count = 0;
        for(int i=0;i<len;i++){
            char tmp = s.at(i);
            if((tmp >= 'A' && tmp <= 'Z') || (tmp >= '0' && tmp <= '9')){
                storage[count] = tmp;
                count ++;
            }else if(tmp >= 'a' && tmp <= 'z'){
                storage[count] = tmp - 32;
                count++;
            }
        }
        for(int j=0;j<int(count/2);j++){
            if(storage[j] != storage[count-1-j]){
                return false;
            }
        }
        return true;
    }
};
