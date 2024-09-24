import heapq
class MedianFinder:

    def __init__(self):
        self.miH,self.maH=[],[]
        heapq.heapify(self.miH)
        heapq.heapify(self.maH)

    def addNum(self, num: int) -> None:
        if len(self.miH)==0:
            heapq.heappush(self.miH,num)
            return
        

        ma=self.miH[0]

        if num>ma:
            heapq.heappush(self.maH,-num)
        else:
            heapq.heappush(self.miH,num)
        
        while len(self.miH)<len(self.maH):
            heapq.heappush(self.miH,-heapq.heappop(self.maH))

        while len(self.miH)<len(self.maH) and len(self.miH)>1:
            heapq.heappush(self.maH,-heapq.heappop(self.miH))

        print(self.miH, self.maH)

    def findMedian(self) -> float:
        ...        


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
#param_2 = obj.findMedian()