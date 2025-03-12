class Solution:
    def tribonacci(self, n: int) -> int:
        m=[0,1,1]
        if n<=2:
            return m[n]
        for i in range(n-2):
            m.append(m[-1]+m[-2]+m[-3])
        return m[-1]
    
s=Solution()
print(s.tribonacci(25))