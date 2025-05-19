from typing import List
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for detail in details:
            age=int(detail[11:13])
            #print(age)
            ans+=1 if age>60 else 0
        return ans

s=Solution()
print(s.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
print(s.countSeniors(["1313579440F2036","2921522980M5644"]))