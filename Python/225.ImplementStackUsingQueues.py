from collections import deque
class MyStack:
    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:        
        self.q.append(x)

    def pop(self) -> int:
        self.rev()
        el=self.q.popleft()
        self.rev()
        return el
        

    def top(self) -> int:
        self.rev()
        el=self.q[0]
        self.rev()
        return el

    def empty(self) -> bool:
        return len(self.q)==0
    
    def rev(self):
        q2=deque()
        while not self.empty():
            q2.append(self.q.pop())
        self.q=q2.copy()

        


obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top()) #2
print(obj.pop()) #2
print(obj.empty()) #False