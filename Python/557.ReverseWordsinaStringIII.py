class Solution:
    def reverseWords(self, s: str) -> str:
        lw=s.split()
        ans=""
        for w in lw:
            ans+=w[::-1] + " "
        return ans.strip()


s=Solution()
print(s.reverseWords("Let's take LeetCode contest"))