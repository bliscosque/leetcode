def sub_sum(arr,target_sum):
    l,r=0,0
    sum=0
    while r<len(arr):
        sum+=arr[r]
        while sum>target_sum and l<r:
            sum-=arr[l]
            l+=1
        if sum==target_sum:
            return arr[l:r+1]
        r+=1
    return None

arr=[10,3,2,5,1,22,1,99]
print(sub_sum(arr,8))
print(sub_sum(arr,22))
print(sub_sum(arr, 200))