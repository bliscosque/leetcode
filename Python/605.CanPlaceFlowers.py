from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0: return True
        flowerbed=[0]+flowerbed+[0]
        for i in range(1,len(flowerbed)-1):
            #print(i,flowerbed[i],flowerbed[i-1],flowerbed[i+1])
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
                if n==0: return True
        return False


s=Solution()
print(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1)) #True
print(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2)) #False