class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds,dt={},{}
        for i,c in enumerate(s):
            if c not in ds:
                ds[c]=[i]
            else:
                ds[c].append(i)
        for i,c in enumerate(t):
            if c not in dt:
                dt[c]=[i]
            else:
                dt[c].append(i)
        #print(ds,dt)
        ms,mt=[],[]
        for v in ds.values():
            ms.append(v)
        for v in dt.values():
            mt.append(v)            
        ms.sort()
        mt.sort()
        return ms==mt


s=Solution()
print(s.isIsomorphic("egg","add"))
print(s.isIsomorphic("foo","bar"))
print(s.isIsomorphic("paper","title"))
print(s.isIsomorphic("bbbaaaba","aaabbbba")) # False