class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp={}
        def int_count(l,c):
            if (l,c) in dp:
                return dp[(l,c)]
            if l==m-1 and c==n-1:
                return 1
            if l>m-1 or c>n-1: 
                return 0
            cnt=int_count(l+1,c)+int_count(l,c+1)
            dp[(l,c)]=cnt
            return cnt
        return int_count(0,0)

s=Solution()
print(s.uniquePaths(3,7))
print(s.uniquePaths(3,2))