# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        a,b=1,n
        while a<=b:
            mid=(a+b)//2
            ans=guess(mid)

            if ans==0: return mid
            elif ans<0:
                b=mid-1
            else:
                a=mid+1
