class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp=[[0 for _ in range(W+1)] for _ in range(n+1)]
        
        for i in range(1,n+1):
            for w in range(1,W+1):
                dp[i][w]=dp[i-1][w] # not include wt
                if wt[i-1]<=w: # can try to include cur weight 
                    dp[i][w]=max(dp[i][w],dp[i-1][w-wt[i-1]]+val[i-1])
                
        return dp[n][W]

        


s=Solution()
print(s.knapSack(4,[4,5,1],[1,2,3],3)) # 3
print(s.knapSack(3,[4,5,6],[1,2,3],3)) # 0