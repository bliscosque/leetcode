from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        n=len(words)
        for i in range(n):
            for j in range(n):
                if i==j: continue
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans

s=Solution()
print(s.stringMatching(words = ["mass","as","hero","superhero"]))
print(s.stringMatching(["leetcode","et","code"])) # ["et","code"]
print(s.stringMatching(["leetcoder","leetcode","od","hamlet","am"])) #["leetcode","od","am"]