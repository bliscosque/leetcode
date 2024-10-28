class Solution:
    def validPalindrome(self, s: str) -> bool:
        def val_int(s1):
            return s1==s1[::-1]
        
        l,r=0,len(s)-1
        used=False
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                s1=s[:l]+s[l+1:]
                s2=s[:r]+s[r+1:]
                return val_int(s1) or val_int(s2)
        return True
        

        
s=Solution()
print(s.validPalindrome("aba")) # True
print(s.validPalindrome("abca")) # True
print(s.validPalindrome("abc")) # False
print(s.validPalindrome("ebcbbececabbacecbbcbe")) # True
