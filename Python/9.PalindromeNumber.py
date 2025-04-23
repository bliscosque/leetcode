class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        s_x=str(x)
        i=0
        j=len(s_x)-1

        while i<j:
            if s_x[i]!=s_x[j]:
                return False
            i+=1
            j-=1

        return True
            

        
s=Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))