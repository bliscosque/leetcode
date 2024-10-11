# using tortoise und hare
class Node:
    def __init__(self, value) -> None:
        self.value=value
        self.next=None

def has_cycle(head):
    if not head or not head.next: 
        return False
    
    slow,fast=head,head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            return True
    
    return False

def find_cycle_start(head):
    if not head or not head.next: 
        return False
    
    slow,fast=head,head
    
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            break
    
    if not fast or not fast.next:
        return None #no cycle... didn't end in break    
    
    # move slow to head and advance both pointers at the same pace
    # This works because we've walked k steps with slow and 2k with fast... so cycle size always divide k
    slow=head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    return slow.value

def cycle_length(head):
    if not head or not head.next: 
        return False
    
    slow,fast=head,head
    
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            break
    
    if not fast or not fast.next:
        return 0 #no cycle... didn't end in break
    
    length=1
    fast=slow.next
    while slow != fast:
        fast=fast.next
        length+=1

    return length

nodes=[Node(i) for i in range(6)]
nodes[0].next = nodes[1]  
nodes[1].next = nodes[2]  
nodes[2].next = nodes[3]  
nodes[3].next = nodes[5]  
nodes[4].next = nodes[3]  
nodes[5].next = nodes[4]  

print("Is there a cycle?",has_cycle(nodes[0]))
print("First node of the cycle:",find_cycle_start(nodes[0]))
print("Length of the cycle:",cycle_length(nodes[0]))