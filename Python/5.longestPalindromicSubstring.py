class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        max_len=1
        ans=s[0]

        # odd
        for i in range(n):
            l,r=i-1,i+1
            #print(i,l,r)
            while l>=0 and r<n:
                ss=s[l:r+1]
                ssr=ss[::-1]
                #print(i,ss, ssr)
                if ss==ssr:
                    new_len=r-l+1
                    if new_len>max_len:
                        ans=ss
                        max_len=new_len
                    l-=1
                    r+=1
                else: 
                    break

        #even
        for i in range(n-1):
            if s[i]==s[i+1]:
                l,r=i,i+1
                #print(i,l,r)
                new_len=r-l+1
                if new_len>max_len:
                    ans=s[l:r+1]
                    max_len=new_len
            else: 
                continue

            while l>=0 and r<n:
                ss=s[l:r+1]
                ssr=ss[::-1]
                if ss==ssr:
                    new_len=r-l+1
                    if new_len>max_len:
                        ans=ss
                        max_len=new_len
                    l-=1
                    r+=1
                else: 
                    break

        return ans



s=Solution()
print(s.longestPalindrome("babad")) # bab
print(s.longestPalindrome("cbbd")) # bb --- FALHA NESTE TC
print(s.longestPalindrome("bb")) # bb
print(s.longestPalindrome("ccc")) # ccc