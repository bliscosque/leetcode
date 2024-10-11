class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans=0
        for i,ch in enumerate(columnTitle[::-1]):
            ans+=(ord(ch)-ord("A")+1)*(26**i)
        return ans


s=Solution()
print(s.titleToNumber("A")) # 1
print(s.titleToNumber("AB")) # 28
print(s.titleToNumber("ZY")) # 701