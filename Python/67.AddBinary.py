class Solution:
    def addBinary(self, a: str, b: str) -> str:
        miL,maxL=min(len(a),len(b)), max(len(a),len(b))
        if len(a)==miL:
            a="0"*(len(b)-miL)+a
        else:
            b="0"*(len(a)-miL)+b
        #print(a,b)
        a=a[::-1]
        b=b[::-1]
        ext=0
        ans=""
        for i in range(maxL):
            s=int(a[i])+int(b[i])+ext
            print(s,a[i],b[i])
            if s==0:
                ans+="0"
                ext=0
            elif s==1:
                ans+="1"
                ext=0
            elif s==2:
                ans+="0"
                ext=1
            else:
                ans+="1"
                ext=1
        if ext==1:
            ans+="1"
        return ans[::-1]
                

s=Solution()
#print(s.addBinary("11","1")) # "100"
#print(s.addBinary("1010","1011")) # "10101"
print(s.addBinary("1111","1111")) # "11110"