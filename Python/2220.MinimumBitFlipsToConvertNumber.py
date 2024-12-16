class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n1=format(start&0xFFFFFFFF, '032b')
        n2=format(goal&0xFFFFFFFF, '032b')
        ans=0
        for i in range(len(n1)):
            if n1[i]!=n2[i]:
                ans+=1
        return ans
    
s=Solution()
print(s.minBitFlips(10,7))