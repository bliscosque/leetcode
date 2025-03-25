class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans=(high-low)//2
        if high%2 or low%2: ans+=1
        return ans
        
s=Solution()
print(s.countOdds(3,7)) #3
print(s.countOdds(8,10)) #1
print(s.countOdds(9,10)) #1