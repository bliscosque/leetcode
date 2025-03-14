from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes=[0,0]
        for b in bills:
            if b==5:
                changes[0]+=1
            elif b==10:
                changes[0]-=1
                changes[1]+=1
                if changes[0]<0: return False
            else:
                if changes[0]>0 and changes[1]>0:
                    changes[1]-=1
                    changes[0]-=1
                elif changes[0]>=3:
                    changes[0]-=3
                else: return False
        return True

s=Solution()
print(s.lemonadeChange(bills = [5,5,5,10,20]))
print(s.lemonadeChange(bills = [5,5,10,10,20]))