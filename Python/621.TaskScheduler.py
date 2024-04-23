from typing import Optional, List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm={}
        for task in tasks:
            hm[task]=1+hm.get(task,0)
        l=[]
        for task,amt in hm.items():
            l.append((-amt,task))
        heapq.heapify(l)
        ans=0
        while len(l)>0:
            n_cur=len(l)

            #print(l, n_cur, ans)

            if len(l) > n:
                n_els=[]
                for i in range(n+1):
                    n_el=heapq.heappop(l)
                    if n_el[0]<-1:
                        n_els.append((n_el[0]+1,n_el[1]))
                for el in n_els:
                    heapq.heappush(l,el)
                ans+=(n+1)
            else:
                n_els=[]
                for i in range(len(l)):
                    n_el=heapq.heappop(l)
                    if n_el[0]<-1:
                        n_els.append((n_el[0]+1,n_el[1]))
                for el in n_els:
                    heapq.heappush(l,el)
                if len(l)>0:
                    ans+=(n+1)
                else:
                    ans+=n_cur
        
        return ans
            


s=Solution()
print(s.leastInterval(["A","A","A","B","B","B"],2)) #8 : A -> B -> idle -> A -> B -> idle -> A -> B.
print(s.leastInterval(["A","C","A","B","D","B"],1)) #6 : A -> B -> C -> D -> A -> B
print(s.leastInterval(["A","A","A", "B","B","B"],3)) #10 : A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

print(s.leastInterval(["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"],7)) #18

