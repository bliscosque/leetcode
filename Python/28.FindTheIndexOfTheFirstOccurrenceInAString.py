class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                found=True
                for j,ch in enumerate(needle):
                    if i+j>=len(haystack) or haystack[i+j]!=ch:
                        found=False
                        break
                if found: 
                    return i
        return -1
    
s=Solution()
print(s.strStr(haystack = "sadbutsad", needle = "sad")) #0
print(s.strStr(haystack = "leetcode", needle = "leeto")) #-1
print(s.strStr(haystack = "aaa", needle = "aaaa")) #-1
        