from typing import List
import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2=len(nums1),len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        if n1 == 0:
            if n2 % 2 == 0:
                return (nums2[n2//2 - 1] + nums2[n2//2]) / 2
            else:
                return nums2[n2//2]
        
        searched_n_elem=(n1+n2)//2+1 if (n1+n2)%2==1 else (n1+n2)//2
        #print("n1",n1,"n2",n2,"searched_n_elem",searched_n_elem)
        s,e=0,n1

        while s<=e:
            sel_n1=(s+e)//2
            #print(s,e,sel_n1)
            sel_n2=searched_n_elem-sel_n1

            #print(sel_n1, sel_n2)

            max_left1=float('-inf') if sel_n1 == 0 else nums1[sel_n1 - 1]
            min_right1=float('inf') if sel_n1 == n1 else nums1[sel_n1]

            max_left2=float('-inf') if sel_n2 == 0 else nums2[sel_n2 - 1]
            min_right2=float('inf') if sel_n2 == n2 else nums2[sel_n2]

            if max_left1<=min_right2 and max_left2 <= min_right1:
                if (n1+n2)%2==1:
                    return max(max_left2, max_left1)
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1>min_right2:
                e=sel_n1-1
            else:
                s=sel_n1+1
                

s=Solution()
print(s.findMedianSortedArrays([1,3],[2])) #2
print(s.findMedianSortedArrays([1,2],[3,4])) #2.5
print(s.findMedianSortedArrays([0,0],[0,0])) #0
print(s.findMedianSortedArrays([2],[])) #2
print(s.findMedianSortedArrays([3,4,5,6],[1,2])) #3.5

