class MyHashSet:

    def __init__(self):
        self.l=[False]*(1000009)
        #print(self.l)

    def add(self, key: int) -> None:
        self.l[key]=True

    def remove(self, key: int) -> None:
        self.l[key]=False

    def contains(self, key: int) -> bool:
        return self.l[key]


obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1)) # True
print(obj.contains(3)) # False
obj.add(2)
print(obj.contains(2)) # True
obj.remove(2)
print(obj.contains(2)) # False