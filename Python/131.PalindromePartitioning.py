from typing import Optional, List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        part=[]

        def isPal(ss):
            return ss==ss[::-1]

        def part_int(pos):
            if pos>=len(s):
                ans.append(part[:])
            for j in range(pos,len(s)):
                if isPal(s[pos:j+1]):
                    part.append(s[pos:j+1])
                    part_int(j+1)
                    part.pop()
        part_int(0)
        return ans    

s=Solution()
print(s.partition("aab")) # [["a","a","b"],["aa","b"]]
