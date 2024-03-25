class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=''
        for ch in s:
            if ch.isalnum():
                newstr+=ch.upper()

        #print(newstr)
        l,r=0,len(newstr)-1
        while l<r:
            if newstr[l]!=newstr[r]: return False
            l+=1
            r-=1
        return True
        

s=Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama")) #true
print(s.isPalindrome("race a car")) #false
print(s.isPalindrome(" ")) # true