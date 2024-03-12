class Solution:
    def findDuplicate(self, nums) -> int:
        hs=set()
        for i in nums:
            if i in hs: return i
            hs.add(i)


s=Solution()
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))
print(s.findDuplicate([3,3,3,3,3]))