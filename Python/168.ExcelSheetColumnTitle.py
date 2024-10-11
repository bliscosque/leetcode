class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=""

        while columnNumber>0:
            letter=chr(ord("A")+(columnNumber-1)%26)
            ans=letter+ans
            columnNumber=(columnNumber-1)//26
            #print(letter,columnNumber)
        return ans

        
s=Solution()
print(s.convertToTitle(1)) # A
print(s.convertToTitle(28)) # AB
print(s.convertToTitle(701)) # ZY