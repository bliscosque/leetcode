class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==0: return 0
        if left==right: return left
        #l and r will be in formar 0000   1[1|0]  [0|1]
        # only the "middle part" should be considered, this middle part should be the same for l and r
        b_left,b_right=bin(left)[2:].zfill(32),bin(right)[2:].zfill(32)
        first_l, first_r=b_left.index('1'), b_right.index('1')
        if first_l!=first_r:
            return 0
        
        finaleq=first_r+1
        while b_left[finaleq]==b_right[finaleq]:
            finaleq+=1
        
        ans=0
        for i in range(first_l, finaleq):
            ans+=2**(32-i-1)*int(b_left[i])
        return ans


        
    
s=Solution()
print(s.rangeBitwiseAnd(5,7)) # 4
print(s.rangeBitwiseAnd(3,3)) # 3
print(s.rangeBitwiseAnd(6,7)) # 6
print(s.rangeBitwiseAnd(10,11)) # 10
print(s.rangeBitwiseAnd(0,0)) # 0
print(s.rangeBitwiseAnd(1,2147483647)) # 0
print(s.rangeBitwiseAnd(600000000,2147483645)) # 0
print(s.rangeBitwiseAnd(3,6)) # 0
