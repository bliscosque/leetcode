from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p): return []
        cntP={}
        cnts_pos={}
        pos=0
        n=len(p)
        ans=[]
        for ch in p:
            cntP[ch]=1+cntP.get(ch,0)
        for i in range(n):
            ch=s[i]
            cnts_pos[ch]=1+cnts_pos.get(ch,0)

        #print(cntP, cnts_pos)
        if cntP==cnts_pos:
            ans.append(pos)
        for i in range(n,len(s)):
            chrem=s[i-n]
            ch=s[i]
            
            cnts_pos[chrem]-=1
            if cnts_pos[chrem]==0: del cnts_pos[chrem]
            cnts_pos[ch]=1+cnts_pos.get(ch,0)

            pos+=1

            if cntP==cnts_pos:
                ans.append(pos)

        return ans

s=Solution()
print(s.findAnagrams(s = "cbaebabacd", p = "abc")) #[0,6]
print(s.findAnagrams(s = "abab", p = "ab")) #[0,1,2]
print(s.findAnagrams("aaaaaaaaaa","aaaaaaaaaaaaa"))