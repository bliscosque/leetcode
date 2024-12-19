            while len(nums)<lastidx and nums[lastidx]==pivot:
                lastidx+=1
            if lastidx<len(nums):
                qs(lastidx,j)