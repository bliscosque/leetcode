class Solution:
    def oneInAnother(self, d1,d2):
        #print(d1,d2)
        for k in d2:
            if d1.get(k,0)<d2[k]: return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        l,r=0,0
        cnt_t={}
        cnt_ss={}
        for c in t:
            cnt_t[c]=1+cnt_t.get(c,0)
        
        possible=False
        st,en,min_len=0,0,float('inf')
        
        # add letters until we have all
        while r<len(s):
            c=s[r]
            cnt_ss[c]=1+cnt_ss.get(c,0)
            #print(cnt_ss)
            while self.oneInAnother(cnt_ss, cnt_t):
                possible=True
                if r-l+1<min_len:
                    st,en=l,r
                    min_len=r-l+1
                cnt_ss[s[l]]-=1
                if cnt_ss[s[l]]==0:
                    del cnt_ss[s[l]]
                l+=1

            r+=1
        
        if not possible:
            return ""
        
        return s[st:en+1]

s=Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC")) # BANC