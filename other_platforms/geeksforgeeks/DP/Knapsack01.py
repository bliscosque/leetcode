class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        memo={}
        def knapSack_int(i, parc_W):
            if (i,parc_W) in memo:
                return memo[(i,parc_W)]
            nonlocal W, n
            if i>=n: 
                return 0

            if parc_W+wt[i]<=W:
                op_include=val[i]+knapSack_int(i+1,parc_W+wt[i])
            else:
                op_include=0

            op_exclude=knapSack_int(i+1,parc_W)

            memo[(i,parc_W)]=max(op_include,op_exclude)

            return memo[(i,parc_W)] 
        
        return knapSack_int(0,0)

s=Solution()
print(s.knapSack(4,[4,5,1],[1,2,3],3)) # 3
print(s.knapSack(3,[4,5,6],[1,2,3],3)) # 0