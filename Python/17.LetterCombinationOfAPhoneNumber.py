from typing import Optional, List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="": return []

        hm={}
        hm["1"]=""
        hm["2"]="abc"
        hm["3"]="def"
        hm["4"]="ghi"
        hm["5"]="jkl"
        hm["6"]="mno"
        hm["7"]="pqrs"
        hm["8"]="tuv"
        hm["9"]="wxyz"
        
        ans=[]
        def lcInt(ss,pos):
            if pos==len(digits):
                ans.append(ss)
                return
            for ch in hm[digits[pos]]:
                lcInt(ss+ch,pos+1)
        lcInt("",0)
        return ans
                      


s=Solution()
print(s.letterCombinations("23"))
