from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1=nums1[:]
        i,j,k=0,0,0
        
        while i<m and j<n:
            if n1[i]<nums2[j]:
                nums1[k]=n1[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
        
        if i<m:
            for l in range(i,m):
                nums1[k]=n1[l]
                k+=1
        if j<n:
            for l in range(j,n):
                nums1[k]=nums2[l]
                k+=1
        
        #print(nums1)

s=Solution()

print(s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))