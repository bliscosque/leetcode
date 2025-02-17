from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printLL(head):
    while head:
        print(head.val,end=" ")
        head=head.next
    print()

    

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next
        
        h=head
        while h and h.next:
            if h.next.val==val:
                h.next=h.next.next
            else:
                h=h.next
        return head

s=Solution()
ll=ListNode(1,ListNode(2,ListNode(6,ListNode(3,ListNode(4,ListNode(5,ListNode(6)))))))
s.removeElements(ll,6)
printLL(ll)
ll2=ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
s.removeElements(ll2,2)
printLL(ll2)