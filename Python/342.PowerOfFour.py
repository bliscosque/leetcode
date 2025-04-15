class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0: return False
        i=0
        while 4**i<=n:
            if 4**i==n: return True
            i+=1
        return False

s=Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(5))
print(s.isPowerOfFour(1))
print(s.isPowerOfFour(8))
print(s.isPowerOfFour(4))