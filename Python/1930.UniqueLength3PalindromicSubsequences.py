class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        cnt={}
        opt=set()
        for ch in s:
            cnt[ch]=1+cnt.get(ch,0)
        for ch in cnt:
            if cnt[ch]>=2:
                f,l=s.index(ch),s.rfind(ch)
                for ch_int in s[f+1:l]:
                    opt.add(ch+ch_int+ch)
        return len(opt)

s=Solution()
print(s.countPalindromicSubsequence("aabca")) #3
print(s.countPalindromicSubsequence("adc")) #0
print(s.countPalindromicSubsequence("bbcbaba")) #4