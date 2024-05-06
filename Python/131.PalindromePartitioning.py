from typing import Optional, List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        for st in range(n):
            for e in range(st+1,n+1):
                ss=s[st:e]
                if ss==ss[::-1]:
                    ans.append(ss)
        return ans
            

s=Solution()
print(s.partition("aab")) # [["a","a","b"],["aa","b"]]
