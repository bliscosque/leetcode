from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        return arr==arr[::-1]

s=Solution()
ll=ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
print(s.isPalindrome(ll))
ll2=ListNode(1,ListNode(2))
print(s.isPalindrome(ll2))