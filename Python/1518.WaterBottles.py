class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty=0
        ans=0
        while numBottles>=1:
            ans+=numBottles
            empty+=numBottles
            
            numBottles=empty//numExchange
            empty=empty%numExchange

        return ans
    
s=Solution()
print(s.numWaterBottles(9,3)) #13
print(s.numWaterBottles(15,4)) #19
