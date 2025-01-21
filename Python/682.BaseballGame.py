from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records=[]
        for op in operations:
            if op=="C":
                records.pop()
            elif op=="D":
                records.append(records[-1]*2)
            elif op=="+":
                records.append(records[-1]+records[-2])
            else:
                records.append(int(op))
        return sum(records)


s=Solution()
print(s.calPoints(operations = ["5","2","C","D","+"]))
print(s.calPoints(operations = ["5","-2","4","C","D","9","+","+"]))
print(s.calPoints(operations = ["1","C"]))