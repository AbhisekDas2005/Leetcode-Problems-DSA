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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if( head->next == NULL)return head ;
        ListNode* temp1=head;
        ListNode* temp2= head->next;
        while(temp2!=NULL){
            int val1=temp1->val;
            int val2=temp2->val;
            while(val2!=0){
                int t=val2;
                val2=val1%val2;
                val1=t;
            }
            ListNode* newn = new ListNode(val1,temp2);
            temp1->next=newn;
            temp2=temp2->next;
            temp1=temp1->next->next;
        }
        return head;
    }
};