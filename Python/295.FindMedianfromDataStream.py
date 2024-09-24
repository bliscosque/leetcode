import heapq
class MedianFinder:

    def __init__(self):
        self.miH,self.maH=[],[]
        heapq.heapify(self.miH)
        heapq.heapify(self.maH)

    def addNum(self, num: int) -> None:
        if len(self.maH)==0:
            heapq.heappush(self.maH,-num)
            return
        

        ma=self.maH[0]

        if num>ma:
            heapq.heappush(self.miH,num)
        else:
            heapq.heappush(self.maH,-num)
        
        while len(self.miH)>len(self.maH) and len(self.miH)>1:
            heapq.heappush(self.maH,-heapq.heappop(self.miH))

        while len(self.miH)<len(self.maH) and len(self.maH) > 1:
            heapq.heappush(self.miH,-heapq.heappop(self.maH))

        #print(self.maH, self.miH)

    def findMedian(self) -> float:
        if len(self.miH)==len(self.maH): 
            return (self.miH[0]-self.maH[0])/2
        elif len(self.miH)>len(self.maH):
            return self.miH[0]
        else:
            return -self.maH[0]

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
#param_2 = obj.findMedian()