class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num+2*t
    
s=Solution()
print(s.theMaximumAchievableX(4,1)) # 6
print(s.theMaximumAchievableX(3,2)) # 7