class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r=1,num
        while l<=r:
            mid=(l+r)//2
            if mid*mid==num: return True
            elif mid*mid>num:
                r=mid-1
            else:
                l=mid+1
        return False
    
s=Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
        
