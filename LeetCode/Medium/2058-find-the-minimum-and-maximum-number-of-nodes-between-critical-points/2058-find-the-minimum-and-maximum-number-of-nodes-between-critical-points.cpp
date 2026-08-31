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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        
        if(head==NULL||head->next==NULL||head->next->next==NULL){
            return {-1,-1};
        }
        vector<int> l={};
        int c=1;
        ListNode* prev=head;
        ListNode* temp=head->next;
        while(temp->next!=NULL){
            int p=prev->val;
            int n=temp->val;
            int next=temp->next->val;

            if((n>p&&n>next)||(n<p&&n<next)){
                l.push_back(c);
            }

            prev=temp;
            temp=temp->next;
            c++;
        }
        if(l.size()<2){
            return {-1,-1};
        }
        int md=INT_MAX;
        for(int i=1;i<l.size();i++){
            md=min(md,l[i]-l[i-1]);
        }
        int maxDist=l[l.size()-1]-l[0];
        return {md,maxDist};
    }
};