class Solution:
    def containsDuplicate(self, nums) -> bool:
        s=set()
        for n in nums:
            if n in s: return True
            else: s.add(n)
        return False

        
s=Solution()
print(s.containsDuplicate([1,2,3,1])) # true
print(s.containsDuplicate([1,2,3,4])) # false
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # true