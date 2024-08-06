from typing import List
from collections import defaultdict
class Solution:
    def countBits(self,i):
        cnt=0
        while i:
            i=i&(i-1)
            cnt+=1
        return cnt
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans=[]
        a=defaultdict(list)
        for el in arr:
            bits=self.countBits(el)
            a[bits].append(el)

        #print(a)
        idxs=list(a.keys())
        idxs.sort()
        for idx in idxs:
            vals=a[idx]
            vals.sort()
            ans+=vals

        return ans
            

s=Solution()
print(s.sortByBits([0,1,2,3,4,5,6,7,8]))
print(s.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))