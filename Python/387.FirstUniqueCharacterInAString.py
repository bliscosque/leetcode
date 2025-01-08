class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm={}
        for ch in s:
            hm[ch]=1+hm.get(ch,0)
        for i,ch in enumerate(s):
            if hm[ch]==1:
                return i
        return -1
        
s=Solution()
print(s.firstUniqChar("leetcode")) #0
print(s.firstUniqChar("loveleetcode")) #2
print(s.firstUniqChar("aabb")) #-1
