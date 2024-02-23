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
        while head is not None and head.next is not None:
            print("in getLast", head.val, head.next.val)
            head=head.next
        n=head
        head.next=None
        print(head.val)
        return n
    
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #while head is not None and head.next is not None and head.next.next is not None:
        n=head.next
        l=self.getLast(head)
        print("last",l)
        head.next=l
        pList(head)
        #head.next.enxt=n
        #head=head.next.next

s=Solution()
l=ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
pList(l)
s.reorderList(l)
pList(l)
