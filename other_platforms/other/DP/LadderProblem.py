# Given a ladder of size N, and an integer K, write a function to compute the number of ways
# to climp the ladder if you can take a jump of at most k at every step.

d={}
def ladder(n,k):
    if n in d: 
        return d[n]
    
    if n==0: return 1

    ans=0
    
    for i in range(1,k+1):
        if n-i>=0:
            ans+=ladder(n-i,k)
    
    d[n]=ans
    return ans

print(ladder(4,3)) # 7
d.clear()
print(ladder(6,3)) # 24
