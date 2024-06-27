class Solution:
    def findMaxSum(self,arr, n):
        if n<=2: 
            return max(arr)
        dp=[0]*n
        dp[0]=arr[0]
        dp[1]=max(arr[1],arr[0])
        for i in range(2,n):
            op1=arr[i]+dp[i-2]
            op2=dp[i-1]
            dp[i]=max(op1,op2)
        #print(dp)
        return dp[-1]

    #     d={}
    #     def f_int(i):
    #         if i in d: return d[i]
    #         nonlocal n
    #         if i>=n: 
    #             return -math.inf
    #         if i==n-1:
    #             return arr[i]
    #         if i==n-2:
    #             return max(arr[i],arr[i+1])
            
            
    #         #including i
    #         op1=arr[i]+f_int(i+2)
    #         #w/o i
    #         op2=f_int(i+1)

    #         d[i]=max(op1,op2)
    #         return d[i]

    #     return f_int(0)


s=Solution()
print(s.findMaxSum([5, 5, 10, 100, 10, 5],6)) #110
print(s.findMaxSum([3, 2, 7, 10],4)) #13