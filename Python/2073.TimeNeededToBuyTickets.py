from collections import deque
from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        pos=0
        ans=0
        while True:
            if tickets[pos]>0:
                ans+=1
                tickets[pos]-=1
                if pos==k and tickets[pos]==0: return ans
            pos+=1
            if pos==len(tickets):
                pos=0
        
    
s=Solution()
print(s.timeRequiredToBuy([2,3,2],2))
print(s.timeRequiredToBuy(tickets = [5,1,1,1], k = 0))