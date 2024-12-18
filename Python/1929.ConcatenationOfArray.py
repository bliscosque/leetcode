from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums+=nums[:]
        return nums

s=Solution()
print(s.getConcatenation([1,2,1]))