# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        s=set()
        while head:
            if head in s: 
                return True
            s.add(head)
            head=head.next
        return False

s=Solution()
l0=ListNode(3,ListNode(2,ListNode(0,ListNode(-4))))
print(s.hasCycle(l0))
l0.next.next.next.next=l0.next
print(s.hasCycle(l0))