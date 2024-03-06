def pList(node):
    if node is None:
        print()
        return
    print(node.val, end='')
    pList(node.next)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) -> ListNode:
        #edge case: list with 1 elem
        if not head.next and n==1:
            head=None
            return head

        last=head
        for i in range(n):
            last=last.next
        
        t_delete=head

        #edge case=delete last elem
        if not last and n==1:
            t_delete.next=None
            return head

        #print(t_delete)
        #print(head)
        # edge case=delete first elem
        if not last:
            head=head.next
            return head

        while (last.next):
            last=last.next
            t_delete=t_delete.next

        t_delete.next=t_delete.next.next
        return head

s=Solution()
l1=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
pList(s.removeNthFromEnd(l1,2))

l2=ListNode(1)
pList(s.removeNthFromEnd(l2,1))

l3=ListNode(1,ListNode(2))
pList(s.removeNthFromEnd(l3,1))

l4=ListNode(1,ListNode(2))
pList(s.removeNthFromEnd(l4,2)) # 2
