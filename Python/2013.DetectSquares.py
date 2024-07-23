from typing import List
class DetectSquares:

    def __init__(self):
        self.points={} # (x,y) -> count

    def add(self, point: List[int]) -> None:
        self.points[(point[0],point[1])]=1+self.points.get((point[0],point[1]),0)

    def count(self, point: List[int]) -> int:
        ans=0
        x,y=point[0],point[1]
        for x1,y1 in self.points:
            if x1==x and y1!=y: #possible point
                d=abs(y1-y)
                #print(d,x,y)
                if ((x1+d,y1) in self.points and (x+d,y) in self.points):
                    ans+=(self.points[(x1+d,y1)]*self.points[(x+d,y)]*self.points[(x1,y1)])
                if ((x1-d,y1) in self.points and (x-d,y) in self.points):
                    ans+=(self.points[(x1-d,y1)]*self.points[(x-d,y)]*self.points[(x1,y1)])
        return ans



obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
print(obj.count([11, 10]))
print(obj.count([14, 8]))
obj.add([11, 2])
print(obj.count([11, 10]))

