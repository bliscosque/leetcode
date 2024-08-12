from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s=set(candyType)
        n=len(candyType)//2
        return min(n,len(s))

s=Solution()
print(s.distributeCandies([1,1,2,2,3,3])) #3
print(s.distributeCandies([1,1,2,3])) #2
print(s.distributeCandies([6,6,6,6])) #1