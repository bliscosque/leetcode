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
    def mergeTwoLists(self, list1, list2):
        ans=ListNode(-1) # not used
        ansHead=ans
        while list1 and list2:
            if list1.val<list2.val:
                ans.next=list1
                list1=list1.next
            else:
                ans.next=list2
                list2=list2.next
            ans=ans.next
        if list1:
            ans.next=list1
        if list2:
            ans.next=list2
        return ansHead.next
            

s=Solution()
l1=s.mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))),ListNode(1,ListNode(3,ListNode(4))))
pList(l1)

l2=s.mergeTwoLists(None,None)
pList(l2)

l2=s.mergeTwoLists(None,ListNode(0))
pList(l2)