class Solution:
    def minOperations(self, s: str) -> int:
        o0,e0=0,0
        o1,e1=0,0
        for i,c in enumerate(s):
            if i%2==0:
                if c=="0":
                    e0+=1
                else: e1+=1
            else:
                if c=="0":
                    o0+=1
                else:
                    o1+=1
        
        return min(o1+e0,e1+o0)


s=Solution()
print(s.minOperations("0100")) #1
print(s.minOperations("10")) #0
print(s.minOperations("1111")) #2