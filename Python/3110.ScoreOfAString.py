class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        for i in range(len(s)-1):
           ans+=abs(ord(s[i+1])-ord(s[i]))
        return ans 
        
s=Solution()
print(s.scoreOfString("hello")) #13
print(s.scoreOfString("zaz")) #50