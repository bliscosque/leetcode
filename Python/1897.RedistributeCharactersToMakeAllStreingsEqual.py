from typing import List
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt={}
        for word in words:
            for ch in word:
                cnt[ch]=1+cnt.get(ch,0)
        n=len(words)
        for ch in cnt:
            if cnt[ch]%n!=0: return False
        return True

s=Solution()
print(s.makeEqual(["abc","aabc","bc"])) #True
print(s.makeEqual(["ab","a"])) #False