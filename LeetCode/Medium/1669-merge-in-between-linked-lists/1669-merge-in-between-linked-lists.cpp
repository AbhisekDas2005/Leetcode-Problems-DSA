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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        int c1=0;
        int c2=0;
        ListNode *temp=list1;
        while(true){
            if (c1==a-1){
                break;
            }
            else{
                temp=temp->next;
                c1+=1;
            }
        }
        ListNode *temp1=list1; 
        while(true){
            if (c2==b+1){
                break;
            }
            else{
                temp1=temp1->next;
                c2+=1;
            }
        }
        ListNode *temp3=list2;
        while(temp3->next!=NULL){
            temp3=temp3->next;
        }
        temp->next=list2;
        temp3->next=temp1;
        return list1;
    }
};