class Solution:
    def twoSum(self, nums, target: int):
        dct={} #num: idx
        for idx,n in enumerate(nums):
            searched=target-n
            if searched in dct:
                return [dct[searched], idx]
            dct[n]=idx

s=Solution()
print(s.twoSum([2,7,11,15],9)) # [0,1] (2+7=9)
print(s.twoSum([3,2,4],6)) # [1,2] 
print(s.twoSum([3,3],6)) # [0,1] 