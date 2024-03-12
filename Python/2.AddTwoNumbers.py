class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pList(node):
    if node is None:
        print()
        return
    print(node.val, end='')
    pList(node.next)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans=ListNode(-1)
        ansHead=ans
        carry=0
        while l1 and l2:
            sum=l1.val + l2.val + carry
            if sum>=10:
                carry=1
                sum=sum%10
            else:
                carry=0
            # print(sum,carry)
            ans.next=ListNode(sum)
            ans=ans.next
            l1=l1.next
            l2=l2.next

        while l1:
            sum=l1.val + carry
            if sum>=10:
                carry=1
                sum=sum%10
            else:
                carry=0
            # print(sum,carry)
            ans.next=ListNode(sum)
            ans=ans.next
            l1=l1.next

        while l2:
            sum=l2.val + carry
            if sum>=10:
                carry=1
                sum=sum%10
            else:
                carry=0
            # print(sum,carry)
            ans.next=ListNode(sum)
            ans=ans.next
            l2=l2.next

        if carry:
            ans.next=ListNode(1)
               
        return ansHead.next



s=Solution()
l1=ListNode(2,ListNode(4,ListNode(3))) #342
l2=ListNode(5,ListNode(6,ListNode(4))) #465
pList(s.addTwoNumbers(l1,l2)) # 807 (rev=708)

l3=ListNode(0)
l4=ListNode(0)
pList(s.addTwoNumbers(l3,l4)) # 0

l5=ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9))))))))) #999999999
l6=ListNode(9,ListNode(9,ListNode(9,ListNode(9)))) #9999
pList(s.addTwoNumbers(l5,l6)) # 89990001

l7=ListNode(2,ListNode(4,ListNode(9)))
l8=ListNode(5,ListNode(6,ListNode(4,ListNode(9))))