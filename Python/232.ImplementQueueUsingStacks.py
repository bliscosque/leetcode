class MyQueue:

    def __init__(self):
        self.q=[]

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        self.rev()
        el=self.q.pop()
        self.rev()

        return el

    def peek(self) -> int:
        self.rev()
        el=self.q[-1]
        self.rev()

        return el

    def empty(self) -> bool:
        return len(self.q)==0

    def rev(self):
        q2=[]
        while self.q:
            q2.append(self.q.pop())
        self.q=q2
        


obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
print(obj.pop())
print(obj.empty())