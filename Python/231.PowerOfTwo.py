class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0: return False
        i=0
        while 2**i <= n:
            if 2**i==n: return True
            i+=1
        return False



s=Solution()
print(s.isPowerOfTwo(1)) # True
print(s.isPowerOfTwo(16)) # True
print(s.isPowerOfTwo(3)) # False
print(s.isPowerOfTwo(-16)) # False
