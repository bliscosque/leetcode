class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        
        positive = x>=0
        if not positive: x=x*-1
        
        while x:
            dig=x%10
            ans=ans*10+dig
            x=x//10
        
        if not positive: ans*=-1
        return ans if -2**31 <= ans <= 2**31-1 else 0

s=Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
