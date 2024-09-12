from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLL(ll):
    if not ll: 
        print("")
        return
    print(ll.val, end=' -> ')
    printLL(ll.next)

class Solution:
    def cleanAndHasLists(self,lists: List[Optional[ListNode]]) -> bool:
        to_delete=[]
        for i,list in enumerate(lists):
            if not list:
                to_delete.append(i)
        for i in to_delete[::-1]:
            del lists[i]
        return len(lists)>0

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans=ListNode()
        ll=ans
        
        while (self.cleanAndHasLists(lists)):
            minVal=lists[0].val
            minList=0
            for i,list in enumerate(lists):
                if list.val < minVal:
                    minVal=list.val
                    minList=i
            ll.next=lists[minList]
            ll=ll.next
            lists[minList]=lists[minList].next
        return ans.next



ll1=ListNode(1,ListNode(4,ListNode(5)))
ll2=ListNode(1,ListNode(3,ListNode(4)))
ll3=ListNode(2,ListNode(6))

s=Solution()
ll=s.mergeKLists([ll1,ll2,ll3])
printLL(ll)