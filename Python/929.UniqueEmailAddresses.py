from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        nmails=set()
        for e in emails:
            #print(e)
            msplit=e.split("@")
            ln,dn=msplit[0],msplit[1]
            ln=ln.replace(".","")
            ln=ln.split("+")[0]
            nmail=ln+"@"+dn
            nmails.add(nmail)
            #print(nmail)
        #print(nmails)
        return len(nmails)

s=Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])) #2
print(s.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])) #3