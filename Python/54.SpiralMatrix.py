from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,c=len(matrix),len(matrix[0])
        layers=min(l,c)//2
        ans=[]
        for layer in range(layers):
            #print(layer, ans,l,c)
            for c1 in range(layer,c-layer):
                ans.append(matrix[layer][c1])
            for l1 in range(layer+1,l-layer):
                ans.append(matrix[l1][c-1-layer])
            # if there is bottom to traverse
            if layer<l-layer-1:
                for c1 in range(c-layer-2,layer-1,-1):
                    ans.append(matrix[l-layer-1][c1])
            # if there is top to traverse
            if layer < c-layer-1:
                for l1 in range(l-layer-2,layer,-1):
                    ans.append(matrix[l1][layer])
        #print(ans)

        # single row or column left
        if min(l,c)%2==1:
            mid=layers
            if l>c:
                for i in range(mid,l-mid):
                    ans.append(matrix[i][mid])
            else:
                for j in range(mid,c-mid):
                    ans.append(matrix[mid][j])
            
        return ans

s=Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]