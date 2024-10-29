from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: 
            return 0
        
        wordList.append(beginWord)
        wordList.append(endWord)
        G={w:[] for w in wordList}

        visited=dict()
        
        n=len(wordList)
        l=len(beginWord)

        for i1 in range(n-1):
            for i2 in range(i1+1,n):
                w1,w2=wordList[i1],wordList[i2]
                diff=0
                for c in range(l):
                    if w1[c]!=w2[c]:
                        diff+=1
                        if diff==2: break
                if diff==1:
                    G[w1].append(w2)
                    G[w2].append(w1)
        #print(G)
        
        dq=deque()
        dq.append(beginWord)
        visited[beginWord]=1
        
        while dq:
            first=dq.popleft()
            for ngb in G[first]:
                if ngb not in visited:
                    dq.append(ngb)
                    visited[ngb]=visited[first]+1
                    if ngb==endWord:
                        #print(visited)
                        return visited[ngb]
        
        return 0



s=Solution()
print(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))