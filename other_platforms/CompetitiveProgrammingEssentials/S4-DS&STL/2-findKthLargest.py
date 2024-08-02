def findKthLargest(nums, k):
    ksmall=len(nums)-k
    l,r=0,len(nums)-1
    while l<=r:
        pivot=nums[l]
        nnums=nums[0:l]
        nnums+=[n for n in nums[l+1:r+1] if n<=pivot]
        pivotpos=len(nnums)
        nnums.append(pivot)
        nnums+=[n for n in nums[l+1:r+1] if n>pivot]
        nnums+=nums[r:]
        if pivotpos==ksmall:
            return pivot
        if pivotpos<ksmall:
            l=pivotpos+1
        else:
            r=pivotpos-1
        nums=nnums
        print(nums, pivotpos)

print(findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
print(findKthLargest([3,2,3,1,2,4,5,5,6], 1)) # 6
print(findKthLargest([7,6,5,4,3,2,1],2)) # 6