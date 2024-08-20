from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s={}
        idx=0
        while head:
            if head in s: 
                return head
            s[head]=idx
            idx+=1
            head=head.next
        return None

s=Solution()
l0=ListNode(3,ListNode(2,ListNode(0,ListNode(-4))))
print(s.detectCycle(l0))
l0.next.next.next.next=l0.next
print(s.detectCycle(l0))