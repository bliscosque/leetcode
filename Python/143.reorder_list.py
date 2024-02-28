# Definition for singly-linked list.

def pList(node):
    if node is None:
        print()
        return
    print(node.val, end='')
    pList(node.next)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getLast(self,head):
        if head is None or head.next is None or head.next.next is None: return None
        while head.next.next is not None:
            #print("in getLast", head.val, head.next.val)
            head=head.next
        n=head.next
        head.next=None
        #print("getLast: ",n.val)
        return n
    
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        while True:
            if head is None or head.next is None: break
            n=head.next
            l=self.getLast(head)
            if l is None: break
            #print("last",l.val)
            head.next=l
            head.next.next=n
            #pList(head)
            head=head.next.next

s=Solution()
l1=ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
s.reorderList(l1)
pList(l1)

l2=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
s.reorderList(l2)
pList(l2)
