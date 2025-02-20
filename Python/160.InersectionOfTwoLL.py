from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hmA={}
        while headA:
            hmA[headA]=headA.val
            headA=headA.next
        while headB:
            if headB in hmA:
                #print(f"Intersected at '{hmA[headB]}'")
                return headB
            headB=headB.next
        #print("No intersection")
        return None

s=Solution()
c=ListNode(8,ListNode(4,ListNode(5)))
a=ListNode(4,ListNode(1,c))
b=ListNode(5,ListNode(6,ListNode(1,c)))
s.getIntersectionNode(a,b)