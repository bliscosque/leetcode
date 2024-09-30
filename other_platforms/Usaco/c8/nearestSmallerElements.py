def nearest_smaller_elem(arr):
    st=[]
    ans=[]
    for el in arr:
        while len(st)>0 and st[-1]>=el:
            st.pop()
        ans.append(st[-1] if len(st)>0 else -1)
        st.append(el)
    return ans

arr=[1,3,5,2,5,3,4,2]
print(nearest_smaller_elem(arr))