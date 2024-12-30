from typing import List
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        max_line=sum(wall[0])
        nrow=len(wall)
        end_pos={}
        maxP=0
        for line in wall:
            s=0
            for b in line[:-1]:
                s+=b
                end_pos[s]=1+end_pos.get(s,0)
                maxP=max(maxP,end_pos[s])
        
        return nrow-maxP 


        


s=Solution()
print(s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])) #2
print(s.leastBricks([[1],[1],[1]])) # 3