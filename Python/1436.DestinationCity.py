from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s=set()
        for orig,dst in paths:
            s.add(dst)
        for orig,dst in paths:
            if orig in s:
                s.remove(orig)
        return s.pop()
        

s=Solution()
print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(s.destCity([["B","C"],["D","B"],["C","A"]]))
