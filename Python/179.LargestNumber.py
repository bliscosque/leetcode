from typing import List
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def f(s1: str,s2: str):
            #print(s1,s2)
            if s1+s2<s2+s1:
                return -1
            elif s1+s2>s2+s1:
                return 1
            else:
                return 0

        n2=[str(n) for n in nums]
        n2.sort(key=cmp_to_key(f), reverse=True)
        st=0

        while st<len(n2) and n2[st]=='0':
            st+=1

        ans=''.join(n2[st:])
        if ans=="": return "0"
        return ans

s=Solution()
#print(s.largestNumber([10,2])) #210
print(s.largestNumber(nums = [3,30,34,5,9])) #"9 5 34 3 30"
print(s.largestNumber(nums = [0,0])) # 0
