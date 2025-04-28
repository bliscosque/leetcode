class Solution:
    def romanToInt(self, s: str) -> int:
        nums={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans=0
        for idx,v in enumerate(s):
            if idx<len(s)-1 and nums[v]<nums[s[idx+1]]:
                ans-=nums[v]
            else:
                ans+=nums[v]
        return ans


s=Solution()
print(s.romanToInt("III")) # 3
print(s.romanToInt("LVIII")) # 58
print(s.romanToInt("MCMXCIV")) # 1994