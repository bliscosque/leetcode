class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        L1,L2=len(str1),len(str2)
        ml=min(L1,L2)
        while (ml>0):
            if L1%ml==0 and L2%ml==0:
                timesL1,timesL2=L1//ml, L2//ml
                #print(str1[ml]*timesL1, str1[ml]*timesL2)
                if str1[0:ml]*timesL1==str1 and str1[0:ml]*timesL2==str2:
                    return str1[0:ml]
            ml-=1
        return ""


s=Solution()
print(s.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(s.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(s.gcdOfStrings(str1 = "LEET", str2 = "CODE"))