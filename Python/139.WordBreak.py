from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans={}
        def f_int(s):
            #print(s)
            if s in ans: return ans[s]
            if s=="": return True
            isPossible=False
            for word in wordDict:
                if s.startswith(word):
                    isPossible=isPossible or f_int(s[len(word):])
            ans[s]=isPossible
            return ans[s]
        f_int(s)
        #print(ans)
        return ans[s]

s=Solution()
print(s.wordBreak("leetcode", ["leet","code"])) #True
print(s.wordBreak("applepenapple", ["apple","pen"])) #True
print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"])) #False
print(s.wordBreak("abcd",["a","abc","b","cd"])) # True