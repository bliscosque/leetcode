from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        
        minlength=999
        minw=""
        for s in strs:
            if minlength>len(s):
                minlength=len(s)
                minw=s
        
        if minlength==0:
            return ""
        
        for minpref in range(1,minlength+1):
            comp=strs[0][:minpref]
            for s in strs[1:]:
                if s[:minpref]!=comp:
                    return comp[:-1]

        return minw

s=Solution()
print(s.longestCommonPrefix(["flower","flow","flight"])) # fl
print(s.longestCommonPrefix(["dog","racecar","car"])) # ""
print(s.longestCommonPrefix([""])) # ""
print(s.longestCommonPrefix(["",""])) # ""
print(s.longestCommonPrefix(["ab","a"])) # "a"