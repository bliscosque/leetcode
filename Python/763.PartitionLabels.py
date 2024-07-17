from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count_all={}
        used_letters=set()
        positions=[]
        for c in s:
            count_all[c]=1+count_all.get(c,0)
        for idx,c in enumerate(s):
            used_letters.add(c)
            count_all[c]-=1
            if count_all[c]==0:
                used_letters.remove(c)
                if len(used_letters)==0:
                    positions.append(idx)
        ans=[positions[0]+1]
        for i in range(1,len(positions)):
            ans.append(positions[i]-positions[i-1])
        return ans


            

s=Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij")) # [9,7,8]
print(s.partitionLabels("eccbbbbdec")) # [10]