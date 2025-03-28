class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_odd=-1
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                last_odd=i
                break
        if last_odd!=-1: 
            first_n_zero=0
            while num[first_n_zero]=='0':
                first_n_zero+=1
            return num[first_n_zero:last_odd+1]
        else: return ""
            
        
s=Solution()
print(s.largestOddNumber("52")) #5
print(s.largestOddNumber("4206")) #""
print(s.largestOddNumber("35427")) #"35427"
