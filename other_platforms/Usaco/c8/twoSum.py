def two_sum(arr,target_sum):
    arr.sort()
    l,r=0,len(arr)-1
    while l<r:
        if arr[l]+arr[r]==target_sum:
            return (arr[l],arr[r])
        while arr[l]+arr[r]>=target_sum and l<r:
            r-=1
        l+=1
    return None



arr=[1,3,2,5,1,1,2,3]
print(two_sum(arr,8))
print(two_sum(arr, 10))
print(two_sum(arr, 4))
print(two_sum(arr, 15))