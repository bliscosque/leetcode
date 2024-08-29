from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        highest_right=[height[0]]
        highest_left=[height[n-1]]

        for i in range(1,n):
            highest_right.append(max(highest_right[i-1],height[i]))
            highest_left.append(max(highest_left[i-1],height[n-i-1]))
        highest_left=highest_left[::-1]
        
        ans=0
        for i in range(1,n-1):
            min_height=min(highest_right[i-1],highest_left[i+1])
            if min_height>height[i]:
                ans+=min_height-height[i]
        return ans


s=Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) #6
print(s.trap([4,2,0,3,2,5])) #9
print(s.trap([0])) #0
print(s.trap([5,4,1,2])) #1
print(s.trap([9,6,8,8,5,6,3])) #3