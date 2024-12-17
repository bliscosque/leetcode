class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.upper()
        old=s[0]
        ans=0
        for ch in s:
            if ch!=old:
                old=ch
                ans+=1
        return ans


s=Solution()
print(s.countKeyChanges("aAbBcC")) #2
print(s.countKeyChanges("AaAaAaaA")) #0