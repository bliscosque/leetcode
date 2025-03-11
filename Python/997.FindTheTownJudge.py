from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dct={i:set() for i in range(1,n+1)}
        trust_no_one={i for i in range(1,n+1)}
        for i,j in trust:
            dct[j].add(i)
            if i in trust_no_one: 
                trust_no_one.remove(i)
        #print(dct)
        for i in dct.keys():
            if len(dct[i])==n-1 and i in trust_no_one:
                return i
        return -1

s=Solution()
print(s.findJudge(n = 2, trust = [[1,2]])) # 2
print(s.findJudge(n = 3, trust = [[1,3],[2,3]])) # 3
print(s.findJudge(n = 3, trust = [[1,3],[2,3],[3,1]])) # -1