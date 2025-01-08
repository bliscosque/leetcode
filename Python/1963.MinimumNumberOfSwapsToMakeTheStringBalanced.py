class Solution:
    def minSwaps(self, s: str) -> int:
        s=list(s)
        n=len(s)
        cnt=0
        ans=0
        j=len(s)-1
        for i in range(n):
            if s[i]=="[": cnt+=1
            else: cnt-=1
            if cnt<0:
                ans+=1
                #pos2=''.join(s).rfind('[')
                while s[j]!="[":
                    j-=1
                s[i],s[j]=s[j],s[i]
                cnt+=2
        return ans

s=Solution()
print(s.minSwaps("][][")) #1
print(s.minSwaps("]]][[[")) #2
print(s.minSwaps("[]")) #0