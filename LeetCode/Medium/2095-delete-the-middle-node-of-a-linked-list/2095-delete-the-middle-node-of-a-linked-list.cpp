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
    ListNode* deleteMiddle(ListNode* head) {
        if (head==NULL || head->next==NULL) {
            return NULL;
        }
        int t=0;
        ListNode* temp=head;
        while (temp!=NULL) {
            temp=temp->next;
            t++;
        }
        int n=t/2;
        ListNode*temp1=head;
        for (int i=0; i<n-1;i++) {
            temp1=temp1->next;
        }
        ListNode* del=temp1->next;
        temp1->next=del->next;
        delete del;
        return head;
    }
};
