from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p,v=set(),set()
        prices=[0]+prices+[0]
        n=len(prices)
        buy_price=-1
        tot=0
        for i in range(1,n-1):
            if prices[i]<prices[i+1] and buy_price==-1: #buy
                buy_price=prices[i]
            elif prices[i]>prices[i+1] and buy_price!=-1: #sell
                tot+=(prices[i]-buy_price)
                buy_price=-1
        return tot

s=Solution()
print(s.maxProfit([7,1,5,3,6,4])) #7
print(s.maxProfit([1,2,3,4,5])) #4
print(s.maxProfit([7,6,4,3,1])) #0
