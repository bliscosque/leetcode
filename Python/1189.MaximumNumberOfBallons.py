class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm={}
        for c in text:
            if c in "balon":
                hm[c]=1+hm.get(c,0)
        if 'l' in hm:
            hm['l']//=2
            if hm['l']==0: return 0
        if 'o' in hm:
            hm['o']//=2
            if hm['o']==0: return 0

        if 'b' not in hm or 'a' not in hm or 'n' not in hm:
            return 0
        
        return min(hm.values())


s=Solution()
print(s.maxNumberOfBalloons("loonbalxballpoon"))