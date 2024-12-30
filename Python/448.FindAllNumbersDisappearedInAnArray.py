from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s={i for i in range(1,n+1)}
        for num in nums:
            if num in s:
                s.remove(num)
        return list(s)
        


s=Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1])) #[5,6]
print(s.findDisappearedNumbers([1,1])) # [2]
