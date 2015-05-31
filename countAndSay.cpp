/*
#########################################################################
## LeetCode Number 70 Count and Say
## Problem description can be found here:
## https://leetcode.com/problems/count-and-say/
## C++ script
#########################################################################
*/

class Solution {
public:
    string countAndSay(int n) {
        if(n==0) return " ";
        if(n==1) return "1";
        std::stringstream ss;
        std::stringstream os;
        ss << n;
        string str = ss.str();
        int length = str.length();
        const char * array = str.c_str();
        int digit= array[0] - 48;
        int times = 1;
        for(int i = 1; i < length; i++){
            if(array[i]==(digit+48)){
                times ++;
            }else{
                os << times << digit;
                digit = array[i]-48;
                times = 1;
            }
        }
        os << times << digit;
        return os.str();
    }
};
