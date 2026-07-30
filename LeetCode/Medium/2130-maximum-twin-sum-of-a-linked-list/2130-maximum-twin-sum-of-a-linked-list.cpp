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
    int pairSum(ListNode* head) {
        ListNode* temp=head;
        int n=0;
        while (temp!=NULL){
            n+=1;
            temp=temp->next;
        }
        int mid=(int)n/2;
        int s[mid];
        temp=head;
        int c=0;
        while (temp!=NULL){
            if (c<mid){
                s[c]=temp->val;
            }
            else{
                s[n-1-c]+=temp->val;
            }
            c+=1;
            temp=temp->next;
        }
        return *std::max_element(s,s+mid);

    }
};