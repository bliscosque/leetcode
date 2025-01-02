class MyHashMap:

    def __init__(self):
        self.l=[-1]*1000009

    def put(self, key: int, value: int) -> None:
        self.l[key]=value

    def get(self, key: int) -> int:
        return self.l[key]

    def remove(self, key: int) -> None:
        self.l[key]=-1


obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
print(obj.get(1)) #1
print(obj.get(3)) #-1
obj.put(2,1)
print(obj.get(2)) #1
obj.remove(2)
print(obj.get(2)) #-1