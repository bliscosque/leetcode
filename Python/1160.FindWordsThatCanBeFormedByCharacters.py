from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_map={}
        ans=0
        for ch in chars:
            chars_map[ch]=1+chars_map.get(ch,0)
        for w in words:
            m={}
            for ch in w:
                m[ch]=1+m.get(ch,0)
            canuse=True
            for ch in m:
                if ch not in chars_map:
                    canuse=False
                    break
                if chars_map[ch]<m[ch]:
                    canuse=False
                    break
            if canuse:
                ans+=len(w)
        return ans


s=Solution()
print(s.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
print(s.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))