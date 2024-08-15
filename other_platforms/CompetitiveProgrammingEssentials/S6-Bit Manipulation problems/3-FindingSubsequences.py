def findSS(s):
    n=len(s)
    maxoverlay=2**n
    ans=[]
    def overlay(i):
        s1=""
        pos=0
        while i:
            last_bit=i%2
            if last_bit:
                s1+=s[pos]
            i=i>>1
            pos+=1
        ans.append(s1)

    for i in range(maxoverlay):
        overlay(i)

    return ans

def findSS_v2(s):
    n = len(s)
    ans=[]
    for i in range(1 << n):
        subset = ''.join(s[j] for j in range(n) if (i & (1 << j)))
        ans.append(subset)
    return ans


print(findSS("abc"))
print(findSS_v2("abc"))