class Solution:
    def maxProfit(self, prices) -> int:
        minPrice=prices[0]
        maxP=0
        for p in prices:
            minPrice=min(minPrice,p)
            maxP=max(maxP,p-minPrice)
        return maxP


s=Solution()
print(s.maxProfit([7,1,5,3,6,4])) # 5
print(s.maxProfit([7,6,4,3,1])) # 0