class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        n1,n2=len(word1),len(word2)
        ans=""
        while i<n1 and j<n2:
            ans+=word1[i]+word2[j]
            i+=1
            j+=1
        while i<n1:
            ans+=word1[i]
            i+=1
        while j<n2:
            ans+=word2[j]
            j+=1
        return ans


s=Solution()
print(s.mergeAlternately(word1 = "abc", word2 = "pqr"))
print(s.mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(s.mergeAlternately(word1 = "abcd", word2 = "pq"))