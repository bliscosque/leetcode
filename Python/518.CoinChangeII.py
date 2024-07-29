from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        def change_int(amount,i=0):
            if (amount, i) in dp:
                return dp[(amount, i)]
            if amount==0: 
                return 1
            if amount < 0:
                return 0
            ans=0
            for c in range(i,len(coins)):
                ans+=change_int(amount-coins[c],c)
            dp[(amount, i)]=ans
            return ans
        return change_int(amount)


s=Solution()
print(s.change(5,[1,2,5])) # 4
print(s.change(3,[2])) # 0
print(s.change(10,[10])) # 1

