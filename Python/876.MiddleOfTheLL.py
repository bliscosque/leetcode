from typing import Optional
# Definition for singly-linked list.
def printLL(head):
    while head:
        print(head.val,end=' ')
        head=head.next
    print()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1,p2=head,head
        while p1.next and p2.next:
            p1=p1.next
            if p2.next.next:
                p2=p2.next.next
            else: 
                return p1
        return p1


ll=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
s=Solution()
printLL(s.middleNode(ll))
ll2=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
printLL(s.middleNode(ll2))