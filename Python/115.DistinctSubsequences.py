class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp={}
        def numDistinct_int(i,j):
            if (i,j) in dp: return dp[(i,j)]
            
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if s[i]==t[j]:
                op1=numDistinct_int(i+1,j+1) #use char
                op2=numDistinct_int(i+1,j) #don't use char
                dp[(i,j)]=op1+op2    
            else:
                dp[(i,j)]=numDistinct_int(i+1,j) #don't use char
            
            return dp[(i,j)]

        return numDistinct_int(0,0)
    
s=Solution()
print(s.numDistinct(s = "rabbbit", t = "rabbit")) #3
print(s.numDistinct(s = "babgbag", t = "bag")) #5


