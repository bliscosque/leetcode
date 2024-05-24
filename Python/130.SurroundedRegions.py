from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l,c=len(board),len(board[0])
        movx=[0,0,1,-1]
        movy=[1,-1,0,0]
        notflip=set()
        visited=set()

        def dfs(i,j):
            visited.add((i,j))
            for k in range(4):
                ni,nj=i+movx[k],j+movy[k]
                if 0<=ni<l and 0<=nj<c:
                    if (ni,nj) not in visited and board[ni][nj]=='O':
                        notflip.add((ni,nj))
                        dfs(ni,nj)
        
        #line 0 and last line
        for j in range(c):
            if board[0][j]=='O':
                notflip.add((0,j))
                dfs(0,j)
            if board[l-1][j]=='O':
                notflip.add((l-1,j))
                dfs(l-1,j)

        #column 0 and last column
        for i in range(l):
            if board[i][0]=='O':
                notflip.add((i,0))
                dfs(i,0)
            if board[i][c-1]=='O':
                notflip.add((i,c-1))
                dfs(i,c-1)

        for i in range(l):
            for j in range(c):
                if (i,j) not in notflip:
                    board[i][j]='X'
        
        

s=Solution()
board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(board)
print(board)

b2=[["X"]]
s.solve(b2)
print(b2)
