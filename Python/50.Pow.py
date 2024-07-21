class Solution:
    def myPow(self, x: float, n: int) -> float:
        def int_pow(x,n):
            if n==0: return 1
            if n==1: return x
            if n==2: return x*x

            if n%2==0:
                ans=int_pow(x,n//2)
                return ans*ans
            else:
                ans=int_pow(x,n-1)
                return ans*x

        return int_pow(x,n) if n>=0 else int_pow(1/x,n*-1)

s=Solution()
print(s.myPow(2,10)) # 1024
print(s.myPow(2.1,3)) # 9.26100
print(s.myPow(2,-2)) # 0.25