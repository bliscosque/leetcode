import math
from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        R,C=len(img),len(img[0])
        ans=[[0 for _ in range(C)] for _ in range(R)] 
        #print(ans)
        for i in range(R):
            for j in range(C):
                s=0
                cnt=0
                for k in range(-1,2):
                    for l in range(-1,2):
                        if 0<=i+k<R and 0<=j+l<C:
                            s+=img[i+k][j+l]
                            cnt+=1
                ans[i][j]=math.floor(s/cnt)
        return ans

s=Solution()
print(s.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))

print(s.imageSmoother([[1,1,1],[1,0,1]]))

print(s.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))

        
                