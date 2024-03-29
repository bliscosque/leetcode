def pList(node):
    if node is None:
        print()
        return
    print(node.val, end='')
    pList(node.next)
    
def pListRev(node):
    if node is None:
        print()
        return
    print(node.val, end='')
    pListRev(node.prev)

class ListNode: 
    def __init__(self, val=0, next=None, prev=None):
        self.val=val
        self.next=next
        self.prev=prev

class DLL: 
    def __init__(self, capacity):
        self.head=None
        self.tail=None
        self.capacity=capacity
        self.num_elem=0

    def add(self, val, hm):
        #add to head

        n=ListNode(val,self.head,None)

        if not self.tail: # 1st elem
            self.tail=n
        if self.head:
            self.head.prev=n

        self.head=n
        self.num_elem+=1

        if self.num_elem>self.capacity:
            #delete tail
            last=self.tail
            print(last, last.val)

            self.tail=last.prev
            self.tail.next=None

            self.num_elem=self.capacity
            # delete from hashmap
            rem_key=[k for k,val in hm.items() if val==last]
            del hm[rem_key[0]]
        
        # return pos os added node
        return n

    def promote(self,node):  # troubleshooting on going in this function
        if not node.prev: # it's already 1st node
            return

        # tail is the node to be promoted
        if self.tail==node and self.num_elem>1:
            self.tail=self.tail.prev
        
        old_head=self.head
        old_prev=node.prev
        old_next=node.next
        
        self.head=node

        self.head.next=old_head
        old_head.prev=node

        if old_prev:
            old_prev.next=old_next
        if old_next:
            old_next.prev=old_prev

        self.head.prev=None
        self.tail.next=None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.dll=DLL(capacity)
        self.hm={}

    def get(self, key: int) -> int:
        if not key in self.hm:
            return -1
        self.dll.promote(self.hm[key])
        #print("Get: ",key)
        #print("For: ")
        #pList(self.dll.head)
        #print("Back: ")
        #pListRev(self.dll.tail)
        return self.hm[key].val
        

    def put(self, key: int, value: int) -> None:
        print('Put: ', key, value)
        if key in self.hm: #already in HM. Just update the value
            node=self.hm[key]
            node.val=value
            self.dll.promote(self.hm[key])
        else:
            n=self.dll.add(value, self.hm) # receives a hm to delete pair if needed
            self.hm[key]=n
        #print("For: ")
        #pList(self.dll.head)
        #print("Back: ")
        #pListRev(self.dll.tail)
        #print('HM: ')
        #print(self.hm)
        #print()
             


# Your LRUCache object will be instantiated and called as such:
#lru = LRUCache(2)
#lru.put(1,1)
#lru.put(2,2)
#print(lru.get(1))

#lru.put(3,3)
#print(lru.get(2))
#lru.put(4,4)
#print(lru.get(1))
#print(lru.get(3))
#print(lru.get(4))

#["LRUCache","put","put","get","put","get","put","get","get","get"]
#[[2],[1,0],[2,2],[1],[3,3],[2],           [4,4],[1],[3],[4]]
#lru2 = LRUCache(2)
#lru2.put(1,0)
#lru2.put(2,2)
#print(lru2.get(1))
#lru2.put(3,3)
#print(lru2.get(2))
#lru2.put(4,4)
#print(lru2.get(1))
#print(lru2.get(3))
#print(lru2.get(4))

#["LRUCache","put","put","get","put","put","get"]
#[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

#lru3=LRUCache(2)
#lru3.put(2,1)
#lru3.put(2,2)

["LRUCache","put","put","put","put","get","get"]
[[2],       [2,1],[1,1],[2,3],[4,1],[1],[2]]

#lru4=LRUCache(2)
#lru4.put(2,1)
#lru4.put(1,1)
#lru4.put(2,3)
