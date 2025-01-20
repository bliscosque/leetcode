class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ns,nt="",""
        for ch in s:
            if ch=="#":
                if len(ns)>0:
                    ns=ns[:-1]
            else:
                ns+=ch
        for ch in t:
            if ch=="#":
                if len(nt)>0:
                    nt=nt[:-1]
            else:
                nt+=ch
        return ns==nt



s=Solution()
print(s.backspaceCompare(s = "ab#c", t = "ad#c")) #True
print(s.backspaceCompare(s = "ab##", t = "c#d#")) #True
print(s.backspaceCompare(s = "a#c", t = "b")) #False