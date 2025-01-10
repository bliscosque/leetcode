from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        l,c=len(matrix),len(matrix[0])
        ms=[]
        for i in range(l):
            ls=[matrix[i][0]]
            for j in range(1,c):
                ls.append(ls[-1]+matrix[i][j])
            if i==0:
                ms.append(ls)
            else:
                to_app=[]
                for j in range(c):
                    to_app.append(ms[i-1][j]+ls[j])
                ms.append(to_app)
        self.ms=ms
        print(ms)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s=self.ms[row2][col2]
        #print(self.ms[row2][col2], self.ms[row2][col1-1], self.ms[row1-1][col2], self.ms[row1-1][col1-1])
        if col1-1>=0:
            s-=self.ms[row2][col1-1]
        if row1-1>=0:
            s-=self.ms[row1-1][col2]
        if col1-1>=0 and row1-1>=0:
            s+=self.ms[row1-1][col1-1]
        return s


obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(obj.sumRegion(1, 1, 2, 2)) #11
print(obj.sumRegion(2, 1, 4, 3)) #8
print(obj.sumRegion(1, 2, 2, 4)) #12