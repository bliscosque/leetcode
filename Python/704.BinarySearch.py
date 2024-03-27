import bisect
class Solution:
    # def search(self, nums, target: int) -> int:
    #     l,r=0,len(nums)-1
    #     while l<=r:
    #         mid=l+(r-l)//2
    #         if nums[mid]==target: return mid
    #         elif nums[mid]>target: r=mid-1
    #         else: l=mid+1
    #     return -1

    def search(self, nums, target: int) -> int:
        pos=bisect.bisect_left(nums,target)
        return pos if 0<=pos<len(nums) and nums[pos]==target else -1

s=Solution()
print(s.search([-1,0,3,5,9,12],9)) #4
print(s.search([-1,0,3,5,9,12],2)) #-1
print(s.search([-1,0,3,5,9,12],13)) #-1