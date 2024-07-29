from typing import List
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def maxProfit_int(i, status, buyPrice=0): # status=[0,1,2], 0=canBuy, 1=canSell, 2=inCooldown
            if (i,status, buyPrice) in dp:
                return dp[(i,status, buyPrice)]
            if i>=len(prices):
                return 0
            if status==0: # can buy here
                op1=maxProfit_int(i+1,1,prices[i]) #buy
                op2=maxProfit_int(i+1,0) # not buy
                dp[(i,status, buyPrice)]=max(op1,op2)
            elif status==1: # can sell here
                op1=prices[i]-buyPrice+maxProfit_int(i+1,2) #sell
                op2=maxProfit_int(i+1,1, buyPrice) # not sell
                dp[(i,status, buyPrice)]=max(op1,op2)
            else: #in cooldown
                dp[(i,status, buyPrice)]=maxProfit_int(i+1,0)

            return dp[(i,status, buyPrice)]

        return maxProfit_int(0,0)            
            

s=Solution()
print(s.maxProfit([1,2,3,0,2])) #3
print(s.maxProfit([1])) # 0
print(s.maxProfit([2,1,4])) # 3