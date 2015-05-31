/*
#########################################################################
## LeetCode Number 21 Merge Two Sorted Lists
## Problem description can be found here:
## https://leetcode.com/problems/merge-two-sorted-lists/
## C++ script
#########################################################################
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* go = new ListNode(0);
        ListNode* head = go;
        if(l1 && !l2) return l1;
        if(!l1 && l2) return l2;
        if(!l1 && !l2) return nullptr;
        
        while(l1 && l2){
            if(l1->val <= l2->val){
                ListNode* tmp = new ListNode(l1->val);
                go->next = tmp;
                go = tmp;
                l1 = l1->next;
            }else{
                ListNode* tmp = new ListNode(l2->val);
                go->next = tmp;
                go = tmp;
                l2 = l2->next;
            }
        }
        
        if(l1) go->next = l1;
        if(l2) go->next = l2;
        return head->next;
    }
};
