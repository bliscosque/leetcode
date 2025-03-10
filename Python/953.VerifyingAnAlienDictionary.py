from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_d=dict()
        for i,ch in enumerate(order):
            ord_d[ch]=i
        nw=len(words)
        for i in range(nw-1):
            w1=words[i]
            w2=words[i+1]
            #print(w1,w2)
            if w1.startswith(w2) and w1!=w2:
                return False
            mins=min(len(w1),len(w2))
            for j in range(mins):
                if w1[j]!=w2[j]:
                    if ord_d[w1[j]]>ord_d[w2[j]]:
                        return False
                    else:         
                        break
        return True

s=Solution()
print(s.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print(s.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(s.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
