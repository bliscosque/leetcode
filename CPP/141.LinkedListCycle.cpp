#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

bool hasCycle(ListNode *head) {
    if (head==NULL) return false;
    set<ListNode*> s;
    ListNode *h=head;
    s.insert(h);
    while (h->next!=NULL)  {
        h=h->next;   
        if (s.count(h)==1) return true;
        s.insert(h);
    } 

    return false;
}

int main() {
    ListNode *l1=new ListNode(3);
    ListNode *ret=new ListNode(2);
    l1->next=ret;
    l1->next->next=new ListNode(0);
    l1->next->next->next=new ListNode(-4);
    l1->next->next->next->next=ret;
    cout << hasCycle(l1) << endl; // true

    ListNode *l2=new ListNode(1);
    l2->next=new ListNode(2);
    l2->next->next=l2;
    cout << hasCycle(l2) << endl; // true
    
    ListNode *l3=new ListNode(1);
    cout << hasCycle(l3) << endl; //false

    ListNode *l4=new ListNode(1);
    l4->next=new ListNode(2);
    cout << hasCycle(l4) << endl; //false
    
    return 0;
}