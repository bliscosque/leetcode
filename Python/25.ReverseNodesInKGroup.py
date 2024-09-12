from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nnodes=0
        ans=ListNode()
        a=ans
        l=head
        while l:
            nnodes+=1
            l=l.next
        print(nnodes)

        l=head
        while nnodes-k>=0:
            nnodes-=k

            changed=[]
            for _ in range(k):
                changed.append(l)
                l=l.next
            
            for e in changed[::-1]:
                a.next=e
                a=a.next
                
        a.next=l

        return ans.next

def printLL(ll):
    if not ll: 
        print("")
        return
    print(ll.val, end=' -> ')
    printLL(ll.next)
    

s=Solution()
ll1=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
ll=s.reverseKGroup(ll1, 2)
printLL(ll)

ll2=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
ll=s.reverseKGroup(ll2, 3)
printLL(ll)

