class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        def lcs_int(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            ans=0
            if text1[i]==text2[j]:
                ans=1+lcs_int(i+1,j+1)
            else:
                ans=max(lcs_int(i+1,j), lcs_int(i,j+1))
            dp[(i,j)]=ans
            return ans

        return lcs_int(0,0)


s=Solution()
print(s.longestCommonSubsequence("abcde", "ace")) #3
print(s.longestCommonSubsequence("abc", "abc")) #3
print(s.longestCommonSubsequence("abc", "def")) #0