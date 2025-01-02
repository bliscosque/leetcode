class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m={}
        m_rev={}
        words=s.split()
        n=len(pattern)
        if n != len(words): 
            return False
        for i in range(n):
            ch,word=pattern[i],words[i]
            #print(ch,word,m, m_rev)
            if ch in m:
                if m[ch]!=word: 
                    return False
            if word in m_rev:
                if m_rev[word]!=ch: 
                    return False
            m[ch]=word
            m_rev[word]=ch
        return True

s=Solution()
print(s.wordPattern(pattern = "abba", s = "dog cat cat dog")) # True
print(s.wordPattern(pattern = "abba", s = "dog cat cat fish")) # False
print(s.wordPattern(pattern = "aaaa", s = "dog cat cat dog")) # False
print(s.wordPattern(pattern = "abba", s = "dog dog dog dog")) # False
print(s.wordPattern(pattern = "abc", s = "dog cat dog")) # False

            
