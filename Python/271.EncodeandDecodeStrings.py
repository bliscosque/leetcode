from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=[]
        for s in strs:
            i=str(len(s)).zfill(3)
            ans.append(i+s)
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            n_pos=int(s[i:i+3])
            i+=3
            ans.append(s[i:i+n_pos])
            i+=n_pos
        return ans

s=Solution()
print(s.decode(s.encode(["neet","code","love","you"])))
print(s.decode(s.encode(["we","say",":","yes"])))