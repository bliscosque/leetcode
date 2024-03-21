class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sol1 = using sort
        #sm=[c for c in s]
        #tm=[c for c in t]
        #sm.sort()
        #tm.sort()
        #return sm==tm

        # Sol2 = using hashmap (dict)
        d1={}
        for c in s:
            if c not in d1: d1[c]=1
            else: d1[c]+=1
        
        for c in t:
            if c not in d1: return False
            elif d1[c]==1:
                del d1[c]
            else:
                d1[c]-=1

        return len(d1)==0

        

s=Solution()
print(s.isAnagram("anagram","nagaram")) #true
print(s.isAnagram("rat","car")) #false
