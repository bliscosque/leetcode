from collections import deque
def slidingWindowMin(A,k):
    q=deque() # (pos,val)
    ans=[]

    for i,cur in enumerate(A):
        while q and cur<=q[-1][-1]: 
            q.pop()
        if q and q[0][0]<=i-k:
            q.popleft()
        q.append((i,cur))
        if i>=k-1: # add in answer from kth item to the end
            ans.append(q[0][-1])
        #print(i,q)
    return ans

arr=[2,1,4,5,3,4,1,2]
print(slidingWindowMin(arr,4))