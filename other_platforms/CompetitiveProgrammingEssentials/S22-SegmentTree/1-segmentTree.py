class SegmentTree:
    def __init__(self, arr) -> None:
        self.n=len(arr)
        self.tree=[0]*(4*self.n) # max elem = 4n
        self._build(arr,1,0,self.n-1) # 1-indexed... fo from 0..n-1 in arr

    def _build(self,arr,v,tl,tr): #tree_left, tree_right
        if tl==tr: #leaf node... store original value of arr
            self.tree[v]=arr[tl]
        else: #go to both parents and build recursivelly
            tm=(tl+tr)//2
            self._build(arr,v*2,tl,tm) 
            self._build(arr,v*2+1,tm+1,tr)
            self.tree[v]=self.tree[v*2]+self.tree[v*2+1]
        
    def update(self,pos,new_val):
        self._update(1,0,self.n-1,pos,new_val)
    
    def _update(self,v,tl,tr,pos,new_val):
        if tl==tr: #leaf... just update val
            self.tree[v]=new_val
        else:
            tm=(tl+tr)//2
            if pos<=tm:
                self._update(v*2,tl,tm,pos,new_val)
            else:
                self._update(v*2+1,tm+1,tr,pos,new_val)
            self.tree[v]=self.tree[v*2]+self.tree[v*2]+1
    
    def query(self,l,r):
        return self._query(1,0,self.n-1,l,r)
    
    def _query(self,v,tl,tr,l,r):
        if l>r:
            return 0
        if l==tl and r==tr: # current node has all value
            return self.tree[v]
        tm=(tl+tr)//2
        return ( 
            self._query(v*2,tl,tm,l,min(r,tm)) + #left subtree 
            self._query(v*2+1,tm+1,tr,max(l,tm+1),r) #right subtree
        )
        

arr=[1,3,5,7,9,11]
st=SegmentTree(arr)
print(st.tree)
print(st.query(1,3))
st.update(2,10)
print(st.query(1,3))