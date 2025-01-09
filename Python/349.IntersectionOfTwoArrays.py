from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1,n2=set(nums1),set(nums2)
        return list(n1.intersection(n2))

s=Solution()
print(s.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))