from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.psum=[nums[0]]
        for n in nums[1:]:
            self.psum.append(self.psum[-1]+n)
        
        print(self.psum)

    def sumRange(self, left: int, right: int) -> int:
        if left==0: return self.psum[right]
        return self.psum[right]-self.psum[left-1]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))

