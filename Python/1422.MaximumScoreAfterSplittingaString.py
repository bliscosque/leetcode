class Solution:
    def maxScore(self, s: str) -> int:
        try_pos=1
        l=s[:try_pos].count('0')
        r=s[try_pos:].count('1')
        max_pnt=l+r
        #print(l,r,max_pnt)
        for i in range(try_pos,len(s)-1):
            if s[i]=='0':
                l+=1
            else:
                r-=1
            #print(i,s[i],l,r)
            max_pnt=max(max_pnt,l+r)
        return max_pnt

s=Solution()
print(s.maxScore("011101")) #5
print(s.maxScore("00111")) #5
print(s.maxScore("1111"))