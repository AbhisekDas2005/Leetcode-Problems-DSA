class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* cur=head->next;
        ListNode* newHead=nullptr;
        ListNode* tail=nullptr;
        int s=0;
        while (cur!=nullptr) {
            if (cur->val==0) {
                ListNode* newn =new ListNode(s);
                if (newHead==nullptr) {
                    newHead=newn;
                    tail=newn;
                } else {
                    tail->next=newn;
                    tail=newn;
                }
                s=0;
            } 
            else {
                s+=cur->val;
            }
            cur=cur->next;
        }
        return newHead;
    }
};