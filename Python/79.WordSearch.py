from typing import Optional, List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        opX=[1,-1,0,0]
        opY=[0,0,-1,1]
        l,c=len(board),len(board[0])
        #print(l,c)

        # used=[[False]*c]*l
        used = [[False for _ in range(c)] for _ in range(l)]
        self.ans=False
        def existInt(x,y,word):
            #print(x,y,word,len(word))
            if word=='': 
                self.ans=True
                return
            if board[x][y]==word[0]:
                if len(word)==1: 
                    self.ans=True
                    return
                used[x][y]=True
                for i in range(4):
                    nx,ny=x+opX[i],y+opY[i]
                    if 0<=nx<l and 0<=ny<c:
                        #print(used)
                        if not used[nx][ny]:
                            #print("trying: ",nx,ny)
                            existInt(nx,ny,word[1:])
                used[x][y]=False
        for i in range(l):
            for j in range(c):
                existInt(i,j,word)
        return self.ans

                
s=Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")) # True
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE")) # True,
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB")) # False