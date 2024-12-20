class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0: return True
        poss=0
        for ch in t:
            if ch==s[poss]:
                poss+=1
                if poss==len(s):
                    return True
        return False
    
s=Solution()
print(s.isSubsequence("abc", t = "ahbgdc")) #True
print(s.isSubsequence("axc", t = "ahbgdc")) #False