class Solution:
    def arrangeCoins(self, n: int) -> int:
        s=0
        i=1
        while s<=n:
            s+=i
            i+=1
        #print(s,i)
        return i-2


s=Solution()
print(s.arrangeCoins(5)) #2
print(s.arrangeCoins(8)) #3
print(s.arrangeCoins(10)) #3