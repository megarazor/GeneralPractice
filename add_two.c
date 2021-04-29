/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdlib.h>
#include <stdio.h>

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    // if (l1->val == 0){
    //     return l2;
    // }
    // else if (l2->val == 0){
    //     return l1;
    // }
    int c= 0;
    struct ListNode *res= malloc(sizeof(struct ListNode));
    struct ListNode *head= res;
    struct ListNode *prev_res= res;
    while (l1 != NULL || l2 != NULL){
        // printf("a\n");
        // printf("input: %d %d\n", l1->val, l2->val);
        if (l1 == NULL){
            res->val= l2->val + c;
        }
        else if (l2 == NULL){
            res->val= l1->val + c;
        }
        else {
            res->val= l1->val + l2->val + c;
        }
        c= res->val / 10;
        // printf("c: %d\n",c );
        res->val= res->val % 10;
        // printf("res: %d\n", res->val);
        struct ListNode *resNext= malloc(sizeof(struct ListNode));
        resNext->next= NULL;
        prev_res= res;
        res->next= resNext;
        res= resNext;
        
        
        // struct ListNode *cur= res;
        // while(1){
        //     printf("%d, ", cur->val);
        //     if (cur->next == NULL) break;
        //     else cur= cur->next;
        // }
        
        if (l1 != NULL)
            l1= l1->next;
        if (l2 != NULL)
            l2= l2->next;
    }
    if (c > 0){
        res->val= c;
        res->next= NULL;
    }
    else{
        // struct ListNode *tmp= res;
        // res= res->next;
        // free(tmp);
        // printf("Ending...\n res: %d, prev_res: %d\n", res->val, prev_res->val);
        free(res);
        prev_res->next= NULL;
    }
    return head;
}
