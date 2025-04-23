class Solution:
    def isUgly(self, n: int) -> bool:
        factors=[2,3,5]
        for factor in factors:
            while n%factor==0 and n!=0:
                n=n//factor
        return n==1

s=Solution()
print(s.isUgly(6))  # True
print(s.isUgly(1))  # True
print(s.isUgly(14)) # False