from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1,s2=set(nums1),set(nums2)
        return [list(s1-s2),list(s2-s1)]

s=Solution()
print(s.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))