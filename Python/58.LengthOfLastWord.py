class Solution:
    def lengthOfLastWord_2(self, s: str) -> int:
        cnt=0
        first=False
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " and not first:
                continue
            elif s[i]==" " and first: 
                break
            cnt+=1
            first=True
        return cnt
    
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

    
s=Solution()
print(s.lengthOfLastWord("Hello World")) #5
print(s.lengthOfLastWord("   fly me   to   the moon  ")) #4
print(s.lengthOfLastWord("a")) #1