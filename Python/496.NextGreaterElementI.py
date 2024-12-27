from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_d={v:i for i,v in enumerate(nums1) }
        nn2=len(nums2)
        ans=[-1]*len(nums1)
        for n2 in range(nn2):
            if nums2[n2] in n1_d:
                gt=-1
                for j in range(n2+1,nn2):
                    if nums2[j]>nums2[n2]:
                        gt=nums2[j]
                        break
                ans[n1_d[nums2[n2]]]=gt
        return ans
                



s=Solution()
print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])) # [-1,3,-1]
print(s.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4])) # [3,-1]