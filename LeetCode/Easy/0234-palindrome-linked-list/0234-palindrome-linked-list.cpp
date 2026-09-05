/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return true;
        }
        ListNode *temp=head;
        std::vector <int> l={};
        while(temp!=NULL){
            l.push_back(temp->val);
            temp=temp->next;
        }
        int n = l.size();
        int li=0;
        int r=n-1;
        while(li<=r){
            if (l[li]!=l[r]){
                return false;
            }
            li++;
            r--;
        }
        return true;
    }
};