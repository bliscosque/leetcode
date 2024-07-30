
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3=len(s1),len(s2),len(s3)
        if l1+l2!=l3: return False
        dp={}
        def isInterleave_int(i,j,k):
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            #print(i,j,k)
            if i==l1:
                dp[(i,j,k)]=s2[j:]==s3[k:]
            elif j==l2:
                dp[(i,j,k)]=s1[i:]==s3[k:]
            elif s1[i]==s2[j]==s3[k]:
                dp[(i,j,k)]=isInterleave_int(i+1,j,k+1) or isInterleave_int(i,j+1,k+1)
            elif s1[i]==s3[k]:
                dp[(i,j,k)]=isInterleave_int(i+1,j,k+1)
            elif s2[j]==s3[k]:
                dp[(i,j,k)]=isInterleave_int(i,j+1,k+1)
            else:
                dp[(i,j,k)]=False
            return dp[(i,j,k)]
        return isInterleave_int(0,0,0)


s=Solution()
print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")) # True
print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc")) # False
print(s.isInterleave(s1 = "", s2 = "", s3 = "")) # True
print(s.isInterleave(s1 = "aaaa", s2 = "aa", s3 = "aaa")) # False