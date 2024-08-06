# You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).
# Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.

import heapq
def maximumScore(a,b,c):
    pq=[-1*a,-1*b,-1*c]
    heapq.heapify(pq)
    pts=0
    while len(pq)>=2:
        a,b=heapq.heappop(pq),heapq.heappop(pq)
        a+=1
        b+=1
        pts+=1
        if a!=0:
            heapq.heappush(pq,a)
        if b!=0:
            heapq.heappush(pq,b)
    
    return pts


print(maximumScore(2,4,6)) # 6
