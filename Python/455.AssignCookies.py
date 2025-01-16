from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ng=len(g)
        ns=len(s)
        cnt=0
        i,j=0,0
        while i<ng:
            while j<ns and g[i]>s[j]:
                j+=1
            if j==ns: return cnt
            cnt+=1
            i+=1
            j+=1
        return cnt

            
                

s=Solution()
print(s.findContentChildren( g = [1,2,3], s = [1,1])) #1
print(s.findContentChildren(g = [1,2], s = [1,2,3])) #2
print(s.findContentChildren(g = [1,2,3], s = [3])) #1