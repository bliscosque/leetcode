class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp={}
        def isMatch_int(s:str,p:str):
            if p=="":
                return s==""
            if (s,p) in dp: return dp[(s,p)]

            ans=False

            first_match=len(s)>0 and (s[0]==p[0] or p[0]==".")
            
            if len(p)>=2 and p[1]=='*':
                #Opc1: ignore p[0]*
                if isMatch_int(s,p[2:]): 
                    ans=True
                #Opc2: check 0..n times 
                else:
                    ans=first_match and isMatch_int(s[1:], p)

            else:
                ans=first_match and isMatch_int(s[1:],p[1:])
            
            dp[(s,p)]=ans
            return ans
            
        return isMatch_int(s,p)

s=Solution()
print(s.isMatch(s = "aa", p = "a")) # False
print(s.isMatch(s = "aa", p = "a.")) # True
print(s.isMatch(s = "aa", p = "a*")) # True
print(s.isMatch(s = "ab", p = ".*")) # True
print(s.isMatch("aab","c*a*b")) # True
print(s.isMatch("mississippi", "mis*is*p*.")) #False
print(s.isMatch(s = "a", p = "ab*")) # True
print(s.isMatch("ab",".*c")) # False
print(s.isMatch("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*")) # True
print(s.isMatch("aaaaaaaaaaaaaaaaaaa","a*a*a*a*a*a*a*a*a*b")) # False