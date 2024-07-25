class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF # 32bits mask in hexa... python handles integer in arbitrary precision

        while b & mask: # b will be carry... so while there is carry
            carry=(a & b) << 1 # there will be a carry when both bits are set... carry will be shifted to the left
            a = (a^b) # sum without carry
            b=carry # for next iter

        return a & mask if b>0 else a


s=Solution()
print(s.getSum(1,2))
print(s.getSum(2,3))
print(s.getSum(20,30))
print(s.getSum(-1,1))