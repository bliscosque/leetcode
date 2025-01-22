class Solution:
    def makeGood(self, s: str) -> str:
        hasmod=True
        while hasmod:
            hasmod=False
            for i in range(len(s)-1):
                if s[i]!=s[i+1] and s[i].lower()==s[i+1].lower() :
                    s=s[0:i]+s[i+2:]
                    hasmod=True
                    break
        return s


s=Solution()
print(s.makeGood(s = "leEeetcode"))
print(s.makeGood("abBAcC"))