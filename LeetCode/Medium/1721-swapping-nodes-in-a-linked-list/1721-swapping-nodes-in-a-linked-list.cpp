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
class Solution{
public:
    ListNode* swapNodes(ListNode* head,int k){
        int l=0;
        ListNode* temp=head;
        while(temp!=NULL){
            l++;
            temp=temp->next;
        }
        int p1=k;
        int p2=l-k+1;
        if(p1==p2)
            return head;
        if(p1>p2)
            swap(p1,p2);
        ListNode* firstprev=NULL;
        ListNode* first=head;
        for(int i=1;i<p1;i++){
            firstprev=first;
            first=first->next;
        }
        ListNode* secondprev=NULL;
        ListNode* second=head;
        for(int i=1;i<p2;i++){
            secondprev=second;
            second=second->next;
        }
        if(firstprev!=NULL)
            firstprev->next=second;
        else
            head=second;
        if(secondprev!=NULL)
            secondprev->next=first;
        ListNode* tempnext=first->next;
        first->next=second->next;
        second->next=tempnext;
        return head;
    }
};