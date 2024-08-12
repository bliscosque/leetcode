class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s,g={},{}
        b,c=0,0
        n=len(secret)
        for i in range(n):
            if secret[i]==guess[i]:
                b+=1
            else:
                s[secret[i]]=1+s.get(secret[i],0)
                g[guess[i]]=1+g.get(guess[i],0)
        #print(s,g)
        for l in s:
            c+=min(s[l],g.get(l,0))
        return f'{b}A{c}B'

s=Solution()
print(s.getHint(secret = "1807", guess = "7810")) # "1A3B"
print(s.getHint(secret = "1123", guess = "0111")) # "1A1B"