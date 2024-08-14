# 1. XOR of 2 unique num will be > 0 (at least 1 bit will be set)
# 2. A bit is set when it's present in exactly one of the two numbers
# 3. We get the position of this set bit and split the original arr in 2 arr (with that set bit and w/o). 
#   One of the numbers will be in 1st, the other in 2nd
# 4. Run XOR again in both arr. As answer, we'll have both numbers


def unique2Num(arr):
    n=len(arr)
    xo=0
    for n in arr:
        xo=xo^n
    pos=0
    while xo&1==0:
        pos+=1
        xo>>1
    # not needed to generate both arrays but it's just for learning purposes
    arr1, arr2=[],[]
    for n in arr:
        if n&(1<<pos): # is pos th bit set?
            arr1.append(n)
        else:
            arr2.append(n)
    ans1=arr1[0]
    ans2=arr2[0]
    for n in arr1[1:]:
        ans1^=n
    for n in arr2[1:]:
        ans2^=n
    return (ans1,ans2)

print(unique2Num([1,3,5,4,3,1,5,7]))