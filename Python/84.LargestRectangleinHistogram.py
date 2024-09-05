from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        max_area=0
        heights.append(0) # will process entire queue

        for i,v in enumerate(heights):
            
            if not st or st[-1][1]<=v:
                st.append((i,v))
            else:
                start=i
                while st and st[-1][1]>v:
                    last_i,last_v=st.pop()
                    area=(i-last_i)*last_v
                    #print(i,v,last_i, last_v, area)
                    max_area=max(max_area,area)
                    start=last_i

                st.append((start,v))
            #print(i,v, st)
        return max_area
    
s=Solution()   
print(s.largestRectangleArea([2,1,5,6,2,3])) # 10
print(s.largestRectangleArea([2,4]))