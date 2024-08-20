class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==0: return 0
        if left==right: return left
        #l and r will be in formar 0000   111  [0|1]
        # only the "common ones" in the middle should be considered
        b_left,b_right=bin(left)[2:].zfill(32),bin(right)[2:].zfill(32)
        first_l=b_left.index('1')
        amt_l=0
        for char in b_left[first_l:]:
            if char=='1':
                amt_l+=1
            else:
                break
        print(first_l,amt_l)
        first_r=b_right.index('1')
        amt_r=0
        for char in b_right[first_r:]:
            if char=='1':
                amt_r+=1
            else:
                break
        print(first_r,amt_r)

        if first_l!=first_r:
            return 0
        
        ansst=first_r
        ansdiff=min(amt_l,amt_r)
        print(ansst,ansdiff)
        
        ans=0
        for i in range(ansst, ansst+ansdiff):
            ans+=2**(32-i-1)
        return ans


        
    
s=Solution()
#print(s.rangeBitwiseAnd(5,7)) # 4
#print(s.rangeBitwiseAnd(3,3)) # 3
#print(s.rangeBitwiseAnd(6,7)) # 6
print(s.rangeBitwiseAnd(10,11)) # 10
#print(s.rangeBitwiseAnd(0,0)) # 0
#print(s.rangeBitwiseAnd(1,2147483647)) # 0
#print(s.rangeBitwiseAnd(600000000,2147483645)) # 0
#print(s.rangeBitwiseAnd(3,6)) # 0
