class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1,-1):
            v=str(i)*3
            if v in num: return v
        return ""
        

s=Solution()
print(s.largestGoodInteger("6777133339")) #777
print(s.largestGoodInteger("2300019")) #000
print(s.largestGoodInteger("42352338")) #""