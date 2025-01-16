from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            n=len(w)
            isPal=True
            for i in range(n//2):
                if w[i]!=w[n-i-1]:
                    isPal=False
            if isPal:
                return w
        return ""

s=Solution()
print(s.firstPalindrome(words = ["abc","car","ada","racecar","cool"])) #ada
print(s.firstPalindrome(words = ["a","car","ada","racecar","cool"])) #ada