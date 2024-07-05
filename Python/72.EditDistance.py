class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        c=len(word1)+1
        l=len(word2)+1
        dp=[[0 for _ in range(c)] for _ in range(l)]
        
        
        for i in range(c):
            dp[0][i]=i
        for i in range(l):
            dp[i][0]=i

        #print(c,l,dp)

        for i in range(1,l):
            for j in range(1,c):
                dp[i][j]=dp[i-1][j]+1
                dp[i][j]=min(dp[i][j],dp[i][j-1]+1)
                if word1[j-1]==word2[i-1]:
                    dp[i][j]=min(dp[i][j],dp[i-1][j-1])
                    #print(i,j,word1[j-1],dp[i][j])
                else:
                    dp[i][j]=min(dp[i][j],dp[i-1][j-1]+1)
        
        return dp[l-1][c-1]

s=Solution()
print(s.minDistance("movie","love")) #2
print(s.minDistance("horse","ros")) #3
print(s.minDistance("intention","execution")) #3