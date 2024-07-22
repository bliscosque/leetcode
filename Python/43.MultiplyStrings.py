class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=[int(n) for n in num1]
        n2=[int(n) for n in num2]
        tmpvals=[]
        maxlen=0
        for i in range(len(n2)-1,-1,-1):
            val=n2[i]
            tmp=[]
            
            for k in range(len(n2)-i-1):
                tmp.append(0)

            carry=0
            for j in range(len(n1)-1,-1,-1):
                v=val*n1[j]+carry
                if v>9:
                    tmp.append(v%10)
                    carry=v//10
                else:
                    tmp.append(v)
                    carry=0
            if carry>0: tmp.append(carry)
            tmpvals.append(tmp.copy())
            maxlen = max(maxlen,len(tmp))
            
        #print(tmpvals)
        ans=[]
        carry=0
        for i in range(maxlen):
            #print(i,carry)
            spos=0
            for psum in tmpvals:
                if len(psum) > i:
                    spos+=psum[i]
            spos+=carry
            #print(i,spos)
            ans.append(spos%10)
            carry=spos//10

        if carry>0:
            ans.append(carry)

        ansstr=''
        first=True
        for i in ans[::-1]:
            ansstr+=str(i)

        while ansstr.startswith('0'):
            ansstr=ansstr[1:]
        if ansstr=='': 
            ansstr='0'
        return ansstr

s=Solution()
print(s.multiply("2","900"))
print(s.multiply("123","456")) # "56088"
print(s.multiply("9","9"))
print(s.multiply("9133","0"))
