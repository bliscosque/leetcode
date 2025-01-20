class Solution:
    def maxProduct(self, s: str) -> int:
        n=len(s)
        
        def genSubsets(L):
            if len(L)==0:
                return [[]]
            smaller=genSubsets(L[:-1])
            extra=L[-1:]
            new=[]
            for small in smaller:
                new.append(small+extra)
            return smaller+new

        sset=genSubsets([i for i in range(n)])
        wordsPal=[]
        for l in sset:
            w=""
            for n in l:
                w+=s[n]
            if w==w[::-1]:
                wordsPal.append((len(l),set(l)))
        lwp=len(wordsPal)
        ans=0
        for i in range(lwp-1):
            for j in range(i+1,lwp):
                l1,w1=wordsPal[i][0],wordsPal[i][1]
                l2,w2=wordsPal[j][0],wordsPal[j][1]

                if l1*l2<=ans:
                    continue

                wsum=w1.union(w2)
                if len(wsum)==l1+l2:
                    ans=max(ans,l1*l2)
        return ans

s=Solution()
print(s.maxProduct("leetcodecom")) #9
print(s.maxProduct("bb")) #1
print(s.maxProduct("accbcaxxcxx")) #25
print(s.maxProduct("dddkkkkddkkd")) #36
print(s.maxProduct("kkkkhhhkkhhh")) #36
