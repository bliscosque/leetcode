class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt={}
        for ch in t:
            cnt[ch]=1+cnt.get(ch,0)
        for ch in s:
            cnt[ch]-=1
            if cnt[ch]==0: del cnt[ch]
        return list(cnt.keys())[0]

s=Solution()
print(s.findTheDifference("abcd", "abcde")) # e
        