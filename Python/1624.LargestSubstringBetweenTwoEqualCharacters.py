class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        cnt={}
        for ch in s:
            cnt[ch]=1+cnt.get(ch,0)
        ans=-1
        for ch in cnt:
            if cnt[ch]>=2:
                p1,p2=s.find(ch),s.rfind(ch)
                ans=max(ans,p2-p1-1)
        return ans


s=Solution()
print(s.maxLengthBetweenEqualCharacters("aa")) #0
print(s.maxLengthBetweenEqualCharacters("abca")) #2 (bc)
print(s.maxLengthBetweenEqualCharacters("cbzxy")) #-1