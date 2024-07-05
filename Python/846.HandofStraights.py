from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort() # dict is ordered by insertion
        d={}
        for el in hand:
            d[el]=d.get(el,0)+1
        
        while len(d)>0:
            st=next(iter(d))
            d[st]-=1
            if d[st]==0: 
                del d[st]
            #print(st)
            for i in range(groupSize-1):
                st+=1
                if st in d:
                    d[st]-=1
                    if d[st]==0: 
                        del d[st]
                else: 
                    return False
        
        return True


        



s=Solution()
print(s.isNStraightHand([1,2,3,6,2,3,4,7,8],3)) #True
print(s.isNStraightHand([1,2,3,6,2,3,4,7,9],3)) #False