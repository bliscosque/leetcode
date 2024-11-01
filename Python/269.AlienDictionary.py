from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        maxlen=0
        n=len(words)
        lengths=[len(w) for w in words]
        maxlen=max(lengths)
        G={}

        # verify prefix violation: ["wrtkj","wrt"]
        for i in range(n-1):
            w1,w2 = words[i], words[i+1]
            # If word if longer than another and prefix, it's invalid
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""

        for w in words:
            for c in w:
                if c not in G:
                    G[c]=set()

        for i in range(n-1):
            w1,w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            for j in range(minLen):
                if w1[j] != w2[j]:
                    G[w1[j]].add(w2[j])
                    break

        #print(G)

        #top sort
        visited={vertex:False for vertex in G}
        stack=[]
        rec_stack = {vertex:False for vertex in G} #check if has cycle

        def dfs(vertex):
            visited[vertex]=True
            
            rec_stack[vertex]=True #for cycle detect
            
            for ngb in G[vertex]:
                if not visited[ngb]:
                    if dfs(ngb): return True
                elif rec_stack[ngb]: return True
            
            rec_stack[vertex]=False
            
            stack.append(vertex)
            
            return False

        cycle=False
        for vertex in G:
            if not visited[vertex]:
                cycle=cycle or dfs(vertex)
        
        if cycle: return ""
        
        return ''.join(stack[::-1])
        

s=Solution()
print(s.foreignDictionary(["z","o"])) #zo
print(s.foreignDictionary(["hrn","hrf","er","enn","rfnn"])) #"hernf"
print(s.foreignDictionary(["wrtkj","wrt"])) # "" #prefix should come first...
print(s.foreignDictionary(["wrt","wrf","er","ett","rftt","te"])) #wertf