from typing import List
from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.tab=[['.' for _ in range(n)] for _ in range(n)]
        self.n=n
        self.ans=[]

        for c in range(self.n):
            self.solveQ(0,c)
        return self.ans
    
    def solveQ(self,i,j):
        print(i,j, self.canQ(i,j))
        if self.canQ(i,j):
            self.tab[i][j]='Q'
            print(self.tab)
            if i==self.n-1:
                a1=deepcopy(self.tab)
                a2=[]
                for l in a1:
                    a2.append(''.join(l))
                self.ans.append(a2)
            else:
                for c in range(self.n):
                    self.solveQ(i+1,c)
            self.tab[i][j]='.'

    
    def canQ(self,i,j):
        for v in range(self.n):
            if self.tab[i][v]=='Q' or self.tab[v][j]=='Q': 
                return False
        
        l,c=i-1,j-1
        while 0<=l<self.n and 0<=c<self.n:
            if self.tab[l][c]=='Q': return False
            l-=1
            c-=1

        l,c=i-1,j+1
        while 0<=l<self.n and 0<=c<self.n:
            if self.tab[l][c]=='Q': return False            
            l-=1
            c+=1

        l,c=i+1,j-1
        while 0<=l<self.n and 0<=c<self.n:
            if self.tab[l][c]=='Q': return False              
            l+=1
            c-=1

        l,c=i+1,j+1
        while 0<=l<self.n and 0<=c<self.n:
            if self.tab[l][c]=='Q': return False               
            l+=1
            c+=1
         

        return True

s=Solution()
print(s.solveNQueens(4))