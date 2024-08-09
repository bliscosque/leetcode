class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor=x^y
        cntbits=0
        while xor:
            xor=xor&(xor-1) # unset last bit
            cntbits+=1
        return cntbits

s=Solution()
print(s.hammingDistance(1,4)) # 2
print(s.hammingDistance(3,1)) # 1