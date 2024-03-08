def pList(node):
    if node is None:
        print()
        return
    print(node.val, end=' ')
    if node.random:
        print(node.random.val, end=' / ')
    else:
        print('',end=' / ')
    pList(node.next)

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nList=Node(-1) #dummy
        nListHead=nList
        dict={}
        dict2={}
        pos=0
        while head:
            dict[head]=pos
            pos+=1
            dict2[head]=head.random

            nList.next=Node(head.val)
            nList=nList.next
            head=head.next

        #print(dict)
        #print(dict2)

        for k,v in dict.items():
            pos_cur=v
            obj_next=dict2[k]
            if obj_next:
                pos_next=dict[obj_next]
            else:
                pos_next=None
                continue
            # print(v, pos_next)
            updating_list=nListHead.next
            updating_pointer=nListHead.next
            for i in range(pos_cur):
                updating_list=updating_list.next
            for i in range(pos_next):
                updating_pointer=updating_pointer.next
            updating_list.random=updating_pointer

        return nListHead.next


s=Solution()
l1=Node(7,Node(13,Node(11,Node(10,Node(1)))))
l1.next.random=l1
l1.next.next.random=l1.next.next.next.next
l1.next.next.next.random=l1.next.next
l1.next.next.next.next.random=l1
pList(l1)

pList(s.copyRandomList(l1))