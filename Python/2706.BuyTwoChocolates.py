from typing import List
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if money>=prices[0]+prices[1]: 
            return money-(prices[0]+prices[1])
        else:
            return money

s=Solution()
print(s.buyChoco(prices = [1,2,2], money = 3))