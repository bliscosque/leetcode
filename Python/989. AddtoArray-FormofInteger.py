from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        k_mat=[]
        while k>0:
            k_mat.append(k%10)
            k//=10
        max_l=max(len(k_mat),len(num))
        ans=[]
        go1=0
        for i in range(max_l):
            n1=num[i] if i<len(num) else 0
            n2=k_mat[i] if i<len(k_mat) else 0
            su=n1+n2+go1
            if su>9:
                go1=1
                su=su%10
            else:
                go1=0
            ans.append(su)
        if go1:
            ans.append(1)
        return ans[::-1]

s=Solution()
print(s.addToArrayForm(num = [1,2,0,0], k = 34)) # [1,2,3,4]
print(s.addToArrayForm(num = [2,7,4], k = 181)) # [4,5,5]
print(s.addToArrayForm(num = [2,1,5], k = 806)) # [1,0,2,1]