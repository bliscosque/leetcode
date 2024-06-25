from typing import List
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d={}

        def f_int(amt):
            if amt==0:
                return 0      
            if amt<0:
                return math.inf   
            if amt in d:
                return d[amt]
            
            ans=math.inf

            for i in coins:
                    ans=min(ans,f_int(amt-i)+1)
            
            d[amt]=ans
            return d[amt]

        ans=f_int(amount)
        return ans if ans!=math.inf else -1


s=Solution()
print(s.coinChange([1,2,5],11)) # 3 (5+5+1)
print(s.coinChange([2],3)) # -1
print(s.coinChange([1],0)) # 0