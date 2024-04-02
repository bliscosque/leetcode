# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pList(l):
    if not l: 
        print()
        return
    print(l.val, end=' -> ')
    pList(l.next)



class Solution:
    def reverseList(self, head):
        # if head is None: return None
        # nHead=head
        # if head.next:
        #     nHead=self.reverseList(head.next)
        #     head.next.next=head
        # head.next=None
        # return nHead
        prev,cur=None,head
        while cur:
            tmp=cur.next # get next before updating it
            cur.next=prev # reverse
            prev=cur # update prev
            cur=tmp # update cur
        return prev
            
        
s=Solution()
l1=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
pList(l1)
l1_1=s.reverseList(l1)
pList(l1_1)