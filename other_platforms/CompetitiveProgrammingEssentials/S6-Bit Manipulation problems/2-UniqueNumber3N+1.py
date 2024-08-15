# Given [] of numbers that repeats 3x and 1 different number, return the non-repeated
# Idea: Count the bits based on positions for all numbers.
# The count will be either 3n or 3n+1. In case it's 3n+1, this is part of the non-repeated number
# Just turn this non repeated number into decimal once again

def n3_1(nums):
    cntbits=[0]*32
    for n in nums:
        pos=0
        while n:
            cntbits[pos]+=(n&1)
            pos+=1
            n=n>>1
    ans=0
    for i in range(32):
        val=cntbits[i]%3
        ans+=val*(2**i)

    return ans

print(n3_1([5,2,5,3,5,2,2]))