def solve(i):
    max1=0
    cur1=0
    lastIsOne=False
    while i:
        lastBit=i&1
        if lastBit:
            if lastIsOne:
                lastIsOne=True
            cur1+=1
            max1=max(max1,cur1)
        else:
            lastIsOne=False
            cur1=0
        i=i>>1

    return max1
                

print(solve(156)) #3