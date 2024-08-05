# this code is fine but it don't pass in LC 215. The only approach that I was able to pass in that TC was by using heapq
import random
def findKthLargest(nums, k):
    def partition(l,r,pivot_idx):
        nums[pivot_idx],nums[r]=nums[r],nums[pivot_idx]
        
        swap_idx=l
        for i in range(l,r):
            if nums[i]<nums[r]:
                nums[i],nums[swap_idx]=nums[swap_idx],nums[i]
                swap_idx+=1
        
        nums[r],nums[swap_idx]=nums[swap_idx],nums[r]
        return swap_idx
    
    def select(l,r,k_smallest):
        if l==r: return nums[l]
        pivot_idx=random.randint(l,r)
        pivot_idx=partition(l,r,pivot_idx)
        if k_smallest==pivot_idx: return nums[k_smallest]
        elif k_smallest<pivot_idx: return select(l,pivot_idx-1, k_smallest)
        else: return select(pivot_idx+1,r,k_smallest)

    return select(0,len(nums)-1, len(nums)-k)


print(findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
print(findKthLargest([3,2,3,1,2,4,5,5,6], 1)) # 6
print(findKthLargest([7,6,5,4,3,2,1],2)) # 6