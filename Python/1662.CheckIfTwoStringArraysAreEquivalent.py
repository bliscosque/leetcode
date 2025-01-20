from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=''.join(word1)
        w2=''.join(word2)
        return w1==w2

s=Solution()
print(s.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"])) #True
print(s.arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"])) #False
print(s.arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"])) #True