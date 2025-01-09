from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s1=sum(students)
        s0=len(students)-s1
        neat=len(students)
        for s in sandwiches:
            if s==1:
                s1-=1
            else:
                s0-=1
            if s1<0 or s0<0:
                return neat
            neat-=1
        return neat


s=Solution()
print(s.countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))
print(s.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))