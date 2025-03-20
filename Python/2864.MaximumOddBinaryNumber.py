class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones=s.count("1")
        zeroes=len(s)-ones
        ans=(ones-1)*"1"+zeroes*"0"+"1"
        return ans

s=Solution()
print(s.maximumOddBinaryNumber("010")) #001
print(s.maximumOddBinaryNumber("0101")) #1001