from typing import List
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]*(amount+1)
        for x in range(1,amount+1):
            dp[x]=math.inf
            for c in coins:
                if x-c >=0:
                    dp[x]=min(dp[x],dp[x-c]+1)
        return dp[amount] if dp[amount]!= math.inf else -1

    def coinChange_reconstruct(self, coins: List[int], amount: int) -> int:
        dp=[0]*(amount+1)
        first=[0]*(amount+1)
        for x in range(1,amount+1):
            dp[x]=math.inf
            for c in coins:
                if x-c >=0 and dp[x-c]+1 < dp[x]:
                    dp[x]=dp[x-c]+1
                    first[x]=c
        
        print(dp)
        print(first)
        # print
        while amount>0:
            print(first[amount])
            amount-=first[amount]
        print()
        return dp[amount] if dp[amount]!= math.inf else -1


s=Solution()
print(s.coinChange_reconstruct([1,2,5],11)) # 3 (5+5+1)
print(s.coinChange([2],3)) # -1
print(s.coinChange([1],0)) # 0