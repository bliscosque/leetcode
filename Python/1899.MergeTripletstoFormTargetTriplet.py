from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        s1,s2,s3=set(),set(),set()
        for x1,x2,x3 in triplets:
            if x1<=target[0] and x2<=target[1] and x3<=target[2]: #triplet can be used
                s1.add(x1)
                s2.add(x2)
                s3.add(x3)
        return target[0] in s1 and target[1] in s2 and target[2] in s3


s=Solution()
print(s.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5])) # True
print(s.mergeTriplets([[3,4,5],[4,5,6]],[3,2,5])) # False
print(s.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5])) # True