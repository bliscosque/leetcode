class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0

        def f_int(i,j):
            nonlocal ans
            if i<0 or j>len(s): 
                return
            if i==j:
                f_int(i-1,j+1)
                return
            st=s[i:j]
            st_r=st[::-1]
            if st==st_r:
                #print(i,j,st)
                ans+=1
                f_int(i-1,j+1)
        
        for i in range(len(s)):
            f_int(i,i+1)
            f_int(i,i)
      

        return ans
            


s=Solution()
print(s.countSubstrings("abc"))
print(s.countSubstrings("aaa"))