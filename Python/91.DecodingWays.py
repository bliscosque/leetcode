class Solution:
    def numDecodings(self, s: str) -> int:
        def f_int(ss):
            #print(ss)

            if len(ss)==0: return 0
            if len(ss)==1: return 1

            # try split 1 char
            s1=int(ss[0])
            s2=ss[1:]
            if s1==0: return 0 # can return directly because both 1 or 2 chars are not valid
            op1=f_int(s2)
            #print("op1",ss, op1)

            # 2 chars (if first char is 0, it will have already returned)
            s1=int(ss[0:2])
            s2=ss[2:]
            if s1>26: op2=0
            elif len(s2)==0: op2=1
            else: op2=f_int(s2)
            #print("op2",ss, op2)

            return op1+op2
        
        return f_int(s)



s=Solution()
print(s.numDecodings("12")) #2
print(s.numDecodings("226")) #3
print(s.numDecodings("06")) #0
print(s.numDecodings("0")) #0 ERRO!!

