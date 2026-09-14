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
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head || head->next==NULL){
            return head;
        }
        int count=1;
        ListNode* con=head;
        while(con->next!=NULL){
            con=con->next;
            count+=1;
        }
        cout<<count;
        for (int i=0;i<(k%count);i++){
            ListNode* temp = head;
            while(temp->next!=NULL && temp->next->next!=NULL){
                temp=temp->next;
            }
            ListNode* temp1 = temp->next;
            temp->next=NULL;
            temp1->next=head;
            head=temp1;
        }
        return head;
    }
};